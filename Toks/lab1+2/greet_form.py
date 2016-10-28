#!/usr/bin/python

import class_SerialPort
import help_module
import bit_stuffing
import time
from class_SerialPort import SerialPort
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
            message = bit_stuffing.bit_stuffing('~'+self.message_field.text()) # CONVERTING
            self.port.write_to_port((message),len(message)) #sending to port

            self.can_read = True #for syncronizing
            self.dialog.append("You: " + self.message_field.text())
            self.message_field.setText("")

    def read_from_port_and_print(self):     # thread which read all info from port
            self.dialog.append(self.port.read_from_port())

    def initial_ports(self,port_name):
        self.port = SerialPort(port_name)

    def get_rate(self):
        return self.port.baundrate()

    def set_rate(self,value):
        self.combo.setCurrentIndex(self.combo.findText(str(value)))
        self.port.set_baundrate(value)

    def can_read(self):
        return self.can_read

    def set_can_read(self,value):
        self.can_read = value

def write_read_message(form1,form2):
    while 1:
        if(form1.can_read):
            form2.read_from_port_and_print()
            form1.set_can_read(False)


def main():
    app = QApplication(sys.argv)

    form = GreetForm(500,400, "/dev/pts/2")
    form_2 = GreetForm(1000,400, "/dev/pts/3")
    _thread.start_new_thread(write_read_message, (form, form_2))
    _thread.start_new_thread(write_read_message, (form_2, form))
    sys.exit(app.exec())

if __name__ == '__main__':
    main()