#!/usr/bin/env python3
import requests
import os, sys
from glob import glob

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
img_path = "./supplier-data/images/"

print("start")

for jimg in glob(img_path + "*"):
    split_filename = os.path.splitext(jimg)
    print ("hello")
    print (split_filename[1])
    if split_filename[1] == '.jpeg':
        print (jimg)
        with open(jimg, 'rb') as opened:
            r = requests.post(url, files={'file': opened})


print("no error")
