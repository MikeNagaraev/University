#!/usr/bin/python

import SerialPort
import Help
import time
from SerialPort import SerialPort
import _thread
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox,QRadioButton, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class GreetForm(QWidget):
    def __init__(self,x,y,port_name):
        self.initial_ports(port_name)
        super(GreetForm, self).__init__()
        self.setGeometry(x, y, 350, 400)
        self.initUI()
        self.can_read = False

    def initUI(self):
        self.create_name_port()
        self.create_combo()
        self.create_mode()
        self.create_dialog()
        self.create_message()
        self.create_okay_button()
        self.setWindowTitle('Chat')
        self.show()

    def create_name_port(self):
        label_name = QLabel(self.port.name, self)
        label_name.x = 10
        label_name.y = 0
        label_name.move(label_name.x,label_name.y)

    def create_combo(self):

        self.label_rate = QLabel("Baundrate:",self)
        self.label_rate.x = 30
        self.label_rate.y = 20
        vbox = QVBoxLayout(self)
        self.combo = QComboBox(self)
        self.combo.x = 30
        self.combo.y = 50
        self.combo.addItem("9600")
        self.combo.addItem("19200")
        self.combo.addItem("38400")
        self.combo.addItem("57600")
        self.combo.addItem("115200")
        self.combo.activated[str].connect(self.port.set_baundrate)
        self.label_rate.move(self.label_rate.x,self.label_rate.y)
        self.combo.move(self.combo.x, self.combo.y)

    def create_mode(self):

        label_mode = QLabel("Mode:",self)
        label_mode.x = 200
        label_mode.y = 20
        label_mode.move(label_mode.x,label_mode.y)

        self.sync_button = QRadioButton("Sync",self)
        self.sync_button.x = 200
        self.sync_button.y = 40
        self.sync_button.move(self.sync_button.x,self.sync_button.y)
        self.async_button = QRadioButton("Async",self)
        self.async_button.x = 200
        self.async_button.y = 60
        self.async_button.move(self.async_button.x,self.async_button.y)

        self.async_button.setChecked(True)
        self.set_mode("Async")
        self.sync_button.toggled.connect(lambda: self.check_mode(self.sync_button))
        self.async_button.toggled.connect(lambda: self.check_mode(self.async_button))

    def create_dialog(self):

        self.dialog = QTextEdit(self)
        self.dialog.setReadOnly(True)
        self.dialog.setLineWrapMode(QTextEdit.NoWrap)
        sb = self.dialog.verticalScrollBar()
        sb.setValue(sb.maximum())
        self.dialog.setGeometry(30,120,250,150)

        label_dialog = QLabel("Dialog:",self)
        label_dialog.move(30, 90)

    def create_message(self):

        label_message = QLabel("Message:",self)
        label_message.move(30, 280)
        self.message_field = QLineEdit(self)
        self.message_field.setGeometry(30,310,250,30)

    def create_okay_button(self):
        btn = QPushButton('Okay', self)
        btn.setGeometry(120, 350, 60, 30)
        btn.clicked.connect(self.push_message)

    def push_message(self):
        if self.message_field.text():
            message = self.port.name + ": " + self.message_field.text()
            self.port.write_to_port(message,len(message)) #sending to port
            self.can_read = True
            self.dialog.append("You: " + self.message_field.text())
            self.message_field.setText("")

    def read_from_port_and_print(self):     # thread which read all info from port
            self.dialog.append(self.port.read_from_port().decode())

    def initial_ports(self,port_name):
        self.port = SerialPort(port_name)

    def check_mode(self,b):
        if b.text() == "Sync":
            if b.isChecked()==True:
                self.set_mode("Sync")
        if b.text() == "Async":
            if b.isChecked()==True:
                self.set_mode("Async")

    def set_mode(self, str):
        if str == "Sync":
            self.sync_button.setChecked(True)
            self.mode = "Sync"
            Help.common_mode = "Sync"
        if str == "Async":
            self.async_button.setChecked(True)
            self.mode = "Async"
            Help.common_mode = "Async"

    def get_mode(self):
        return self.mode

    def get_rate(self):
        return self.port.baundrate()

    def set_rate(self,value):
        self.combo.setCurrentIndex(self.combo.findText(str(value)))
        self.port.set_baundrate(value)

    def can_read(self):
        return self.can_read

    def set_can_read(self,value):
        self.can_read = value


def check_settings(form1,form2):
    while 1:
        if(Help.common_mode == "Sync"):
            form2.set_rate(form1.get_rate())
        form1.set_mode(Help.common_mode)
        form2.set_mode(Help.common_mode)
        time.sleep(0.1)


def write_read_message(form1,form2):
    while 1:
        if(form1.can_read):
            form2.read_from_port_and_print()
            form1.set_can_read(False)


def main():
    app = QApplication(sys.argv)

    form = GreetForm(500,400, "/dev/pts/1")
    form_2 = GreetForm(1000,400, "/dev/pts/2")
    _thread.start_new_thread(check_settings,(form, form_2))
    _thread.start_new_thread(write_read_message, (form, form_2))
    _thread.start_new_thread(write_read_message, (form_2, form))
    sys.exit(app.exec())

if __name__ == '__main__':
    main()