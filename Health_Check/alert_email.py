#!/usr/bin/env python3
import psutil
import socket
import alert_email
import os

subject_line = ""

#report error if over 80%
cpu = psutil.cpu_percent()
if cpu > 80:
    subject_line = "Error - CPU usage is over 80%"
    print("CPU is ", cpu) #result is in %

#report error if lower than 20%
disk = psutil.disk_usage('/')
if 100-disk[3] < 20:
    subject_line = "Error - Available disk space is less than 20%"
    print("Disk is ", disk[3]) #result is in % of usage

#report error if less than 500M = 4,096,000byte
vm = psutil.virtual_memory()
if vm[6] < 4096000:
    subject_line = "Error - Available memory is less than 500MB"
    print("VM is ", vm[6])

#report error if not able to resolve 127.0.0.1
local_add = socket.gethostbyname('localhost')
if local_add != "127.0.0.1":
    subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
    print("Network Address is", local_add)


#send email alert
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = subject_line
body = "Please check your system and resolve the issue as soon as possible"

message = alert_email.generate(sender, receiver, subject, body)
alert_email.send(message)

#direct copy from car.py
if __name__ == "__main__":
    main(sys.argv)
