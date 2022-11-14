from pickle import TRUE
import serial.tools.list_ports


serialInst = serial.Serial('COM6', 9600)


# serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf-8').rstrip())
