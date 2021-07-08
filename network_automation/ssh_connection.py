from pyfiglet import Figlet

import paramiko
import os.path
import time
import sys
import re

poisonFont = Figlet(font='poison', width=1000)

print(poisonFont.renderText("Conf_Net"))

#Check username/password file
#Prompt user for input - path of username/password file
user_file = input("\n# Please enter 'user file' path and name (e.g. - /Users/myuser/documents/myfile.txt): ")

#Verify input is valid file and path
if os.path.isfile(user_file) == True:
    print("\n\t* Username/password file is valid! \n")
else:
    print("\n\t* File {user_file} does not exist! Please check your file path and try again!\n".format(user_file=user_file))
    sys.exit()

#Check commands file
#Prompt user for input - path of commands file
cmd_file = input("\n# Please enter 'commands file' path and file name (e.g. - /Users/myuser/documents/myfile.txt): ")

#Verify input is valid file and path
if os.path.isfile(cmd_file) ==  True:
    print("\n\t* Commands file is valid! \n")
else:
    print("\n\t* File {cmd_file} does not exist! Please check your file path and try again!\n".format(cmd_file=cmd_file))
    sys.exit()

#Create SSHv2 connection
def ssh_connection(ip):
    global user_file
    global cmd_file

    try:
        with open("user_file") as selected_user_file:
            selected_user_file.seek(0)
            username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

            selected_user_file.seek(0)
            password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

            #Log in to device/start ssh session
            session = paramiko.SSHClient()
            
            #For testing purposes-- allows auto-accepting of unknown host keys.
            #Do not use in Production!
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            #Set ip, username, and password for connection
            session.connect(ip.rstrip('\n'), username = username, password = password)

            #Start interactive shell session on the device
            connection = session.invoke_shell()
            time.sleep(.1)

            #Set terminal length for output - disable pagination
            connection.send("enable\n")
            time.sleep(.1)
            connection.send("terminal length 0\n")
            time.sleep(.1)

            #Enter global config mode
            connection.send("\n")
            connection.send("configure terminal\n")
            time.sleep(.1)

            #Send command file as input to terminal
            with open("cmd_file") as selected_cmd_file:
                selected_cmd_file.seek(0)

                for each_line in selected_cmd_file:
                    connection.send(each_line + '\n')
                    time.sleep(1)

            #Check command output for IOS syntax errors
            terminal_output = connection.recv(65535)

            if re.search(b"% Unknown command or computer name, or unable to find computer address", terminal_output):
                print("* There was at least one IOS syntax error on device {ip} ".format(ip = ip) + "See output below: \n")
            else:
                print('\n* ####DONE FOR DEVICE {ip}#### *'.format(ip = ip))

            #Return terminal output line by line as a string
            cleaner_terminal_output = terminal_output.decode()
            print(cleaner_terminal_output)

            #Close connection
            session.close()

    except paramiko.AuthenticationException:
        print("\n### Invalid username or password ### \n\n\t* Please check username/password credentials in 'user_file'.  \n\t* Also, check the device configuration (e.g. username admin secret p@ssw0rd) \n\n# Closing program ")        
