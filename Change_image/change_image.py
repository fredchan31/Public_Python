#!/usr/bin/env python3


import os, sys
from PIL import Image
from glob import glob

img_path = "./supplier-data/images/"


print("start")

for file in glob(img_path + "*"):
	split_filename = os.path.splitext(file)
	print (split_filename[1])
	if split_filename[1] == '.tiff':
		outfile_name = split_filename[0] + ".jpeg"
		print(split_filename[0])
		with Image.open(file) as im:
			new_im = im.convert('RGB')
			print(new_im.mode)
			new_im.resize((600,400)).save(outfile_name)




print("no error")
