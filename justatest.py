##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed
import serial  # sudo pip install pyserial should work

serial_port = 'COM3';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt";

output_file = open(write_to_file_path, "w+",encoding="UTF-8",errors="ignore");
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    line = line.decode('UTF-8', errors="ignore") #ser.readline returns a binary, convert to string
    print(line);
    output_file.write(line);