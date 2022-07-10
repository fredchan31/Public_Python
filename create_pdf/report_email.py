#!/usr/bin/env python3

import emails
import os, datetime
import reports
from datetime import date
import operator
from operator import itemgetter


#this is used to send out the pdf created in the reports.py
today = date.today()
txt_path = "./supplier-data/descriptions/"
txt_dirs = os.listdir(txt_path)
pdf_path = "./supplier-data/descriptions/" # /tmp/

extract_data = []
table_data = []


for txt_file in txt_dirs:
    split_filename = os.path.splitext(txt_file)
    if split_filename[1] == '.txt':
        with open(txt_path + txt_file, "r", encoding='latin1') as content:
            value = content.readlines(0)
            extract_data.append(['name: ', value[0].rstrip('\n'), 'weight: ', value[1].rstrip('\n')])

extract_data = sorted(extract_data, key=itemgetter(1), reverse=False)
print(extract_data)
#organise table in according to the formate request
for data in extract_data:
    table_data.append([data[0], data[1]])
    table_data.append([data[2], data[3]])
    table_data.append([""])

pdf_full_path = pdf_path + "process.pdf"
process_date = today.strftime("%B %d, %Y")
title = "Processed Update on " + process_date

print(table_data)
if __name__ == "__main__":
    reports.generate(pdf_full_path, title, table_data)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, pdf_full_path)
    emails.send(message)
