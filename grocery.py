#!/usr/bin/python

# Current time and temperature display for Raspberry Pi w/Adafruit Mini
# Thermal Printer.  Retrieves data from DarkSky.net's API, prints current
# conditions and time using large, friendly graphics.
# See forecast.py for a different weather example that's all text-based.
# Written by Adafruit Industries.  MIT license.
#
# Required software includes Adafruit_Thermal, Python Imaging and PySerial
# libraries. Other libraries used are part of stock Python install.
#
# Resources:
# http://www.adafruit.com/products/597 Mini Thermal Receipt Printer
# http://www.adafruit.com/products/600 Printer starter pack

from __future__ import print_function
from Adafruit_Thermal import *
import urllib.request, json

# Global
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

print("Grocery List Print Requested")

# Fetch grocery data from Grocery Rails Program, parse resulting JSON
response = urllib.request.urlopen("http://127.0.0.1:3000/groceries.json")
grocery_list = json.loads(response.read())
# print(grocery_list)

all_categories = ['Produce', 'Bread', 'Meat', 'Prepared food', 'Dairy', 'Frozen', 'Toiletries', 'Aisle', 'Other']

grocery_list.sort(key=lambda x: x['category']) 


category = 0
array_length = len(all_categories)

for category in range(array_length):
    print(all_categories[category])
    # Category print
    printer.feed(1)    
    printer.inverseOn()
    printer.boldOn()
    printer.print(all_categories[category])
    # Reset size
    printer.inverseOff()
    printer.boldOff()			
    for grocery in grocery_list:
        if int(grocery['category']) == int(category):
            print(grocery['name'])
            # Each Grocery
            printer.print(grocery['name'])

printer.feed(3)

