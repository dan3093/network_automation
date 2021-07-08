import os.path
import sys


#Check IP address file and content validity
def ip_file_valid():
      
    #prompt user for input
    ip_file = input("\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")

    #check if file exists
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :) \n")
    else:
        print("\n* File {} does not exist :( Please check and try again.\n".format(ip_file))

    #Open user selected file for reading (IP addresses file)
    with open(ip_file, "r") as selected_ip_file:
        selected_ip_file.seek(0)
        ip_list = selected_ip_file.readlines()

    return ip_list         
   