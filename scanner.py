import socket
#import RPi.GPIO as GPIO
from time import sleep
import os


#Raspberry Pi Led
'''GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)
sleep(1)
GPIO.output(21, GPIO.LOW)'''


#Function for scanning
def fullscan(ip):
    for port in range(1,1000):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result = sock.connect_ex((ip,port))
        
        if result == 0:
            with open("scanned.txt", "a") as file:
                file.write(ip + "\t" + str(port) + ": Open\n")
        sock.close()

#Extract self ip address
def getIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

upHosts = []

myIp = getIpAddress()
splitedMyIp = myIp.split(".")
ipToScan = splitedMyIp[0] + "." + splitedMyIp[1] + "." + splitedMyIp[2] + "."

for i in range(255):
    response = os.system("ping -c 1 " + ipToScan + str(i))
    if response == 0:
        print(i)
        upHosts.append(i)
print(ipToScan)
for i in upHosts:
    print(ipToScan + str(i))
    fullscan(ipToScan + str(i))

#GPIO.output(21, GPIO.HIGH)