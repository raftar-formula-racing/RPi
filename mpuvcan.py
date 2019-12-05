# to set up vcan:
# sudo modprobe vcan
# sudo ip link add dev vcan0 type vcan
# sudo ip link set up vcan0
import struct
import can
import csv
bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
# notifier = can.Notifier(bus, [can.Printer()])
while True:
	msg = bus.recv()
	[x]=struct.unpack('f', msg.data)
	print("Time: :", msg.timestamp, "Msg: ", x, "ID: ", msg.arbitration_id)
	row = [ msg.timestamp,x, msg.arbitration_id]
	with open('canlog.csv', 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)
	csvFile.close()
