"""She bangs line for linux"""
#! /usr/bin/env python3

"""Imports necessary Libraries"""
import os
import requests


"""get txt data from feedback using determined dir below"""
data_text = os.listdir('/data/feedback')

"""Library to contain the data from txt"""
result_dict = {}

"""Subpart of file as a key for dictionary"""
key_values = ("title","name","date","feedback")

"""Loop through each file in the dir"""
for file in data_text:
        files = open('/data/feedback/'+file, "r")
        count = 0
	"""Loop through content of file with respective key from dict"""
        for lines in files:
                if count == 0:
                        result_dict['title'] = lines
                elif count ==1:
                        result_dict['name'] = lines
                elif count == 2:
                        result_dict['date'] = lines
                else:
                        result_dict['feedback'] = lines
                count=count+1
	"""POST request to post the data from dictionary from txt data"""
        response = requests.post(r'http://34.69.245.175/feedback/', json=result_dict)
        print('Response',response.status_code)
        files.close()
