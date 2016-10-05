#!/usr/bin/python


import serial
import help_module
import bit_stuffing
from bitstring import BitArray

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
        return bit_stuffing.back_convert(BitArray(self.ser.read(help_module.X)).bin)

    def write_to_port(self,str,length):
        help_module.X = length
        self.ser.write(str)

    def name(self):
        self.name

    def baundrate(self):
        return self.ser.baudrate