import serial
import io

serial_port_1 = serial.Serial("/dev/pts/1",9600)
serial_port_2 = serial.Serial("/dev/pts/2")
while 1:
    str = input("Write message: ");

    serial_port_2.write(str.encode());
    print(serial_port_1.read(len(str)).decode());

