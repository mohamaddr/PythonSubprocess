import sys
import subprocess
import os
from decouple import config


proc = subprocess.Popen(['ping', 'IPAddress'], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    print(line)
    decode = line.decode('utf-8')
    if 'time=' in decode:
        break

connected_ip = line.decode('utf-8').split()[3]
print(connected_ip)
if connected_ip == 'IPAddress:':
    subprocess.Popen(['say','your device has joined the network'])

