#! /usr/bin/env python3
import os
import requests
import json

#List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
txt_path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"
ip = "http://35.184.33.47"
txt_dirs = os.listdir(txt_path)
img_dirs = os.listdir(img_path)

print("start")

for txt_file in txt_dirs:
	print(txt_file)
	split_filename = os.path.splitext(txt_file)
	if split_filename[1] == ".txt":
		dict = {"name": "", "weight": "", "description": "", "image_name": ""}

		print (split_filename[0])
		with open(txt_path + txt_file, "r", encoding="utf-8") as content:
			value = content.readlines(0)

			dict["name"] = value[0].rstrip('\n')
			dict["weight"] = value[1].rstrip(" lbs\n")
			dict["description"] = value[2].rstrip('\n')
			dict["image_name"] = split_filename[0] + '.jpeg'

#			dict = json.dumps(dict) #convert dictionary to json
			print (dict)
			url = ip + "/fruits/"
			response = requests.post(url, data=dict)
			print(response.request.body)
			if response.status_code != 201:
				raise Exception('POST error status={}'.format(response.status_code))
			print('Created feedback ID: {}'.format(response.json()["id"]))


print("Success!")
