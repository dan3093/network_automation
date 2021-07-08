from datetime import datetime
from pyfiglet import Figlet
import os
import re

poisonFont = Figlet(font='poison')

current_time = str(datetime.now())

with open("test_file", "w") as file1:
    file1.write((poisonFont.renderText("Danno is amazing")))

#my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'    

#a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
#print(a.group(0))
