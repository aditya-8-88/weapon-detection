import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import json
def branchLocation(lat,long):
    # lat =  28.6118798325174
    # long =  77.0378093011461
    url = f'https://www.google.com/maps/search/?api=1&query={lat},{long}'
    webbrowser.register('firefox',
            None,
            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open(url)

def check_for_new_files(directory):
    with open("output/data.json","r") as rf:
        data= json.load(rf)
    filename="data.json"
    while True:
        if os.path.isfile(os.path.join(directory, filename)):
            print(data['lat'])
            print(data['long'])
            branchLocation(data['lat'],data['long'])
            break
        time.sleep(1)
        print("not get")

directory= r"Z:\Banking--main\Banking--main\Banking--main\output"
check_for_new_files(directory)
# branchLocation()