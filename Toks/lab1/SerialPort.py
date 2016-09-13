#!/usr/bin/python


import serial
import Help
class SerialPort:

    def __init__(self, name):
        self.name = name
        self.create()

    def create(self):
        self.ser = serial.Serial(self.name)
        self.ser.baudrate = 9600

    def set_baundrate(self, value):
        self.ser.baudrate = int(value)

    def read_from_port(self):
        return self.ser.read(Help.X)

    def write_to_port(self,str,length):
        Help.X = length
        self.ser.write(str.encode())

    def name(self):
        self.name

    def baundrate(self):
        return self.ser.baudrate