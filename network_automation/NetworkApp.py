import sys
from pyfiglet import Figlet

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_address_valid
from ip_reach_custom import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads




#Save the list of IP addresses in "ip_list_file" to a variable
ip_list = ip_file_valid()

#test list of IP addresses to ensure they are valid
try:
    ip_address_valid(ip_list)    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Verify reachability of each IP in ip_list
#try:
 #   ip_reach(ip_list)
#except KeyboardInterrupt:
  #  print("\n\n* Program aborted by user. Exiting...\n")
   # sys.exit()    

#Call threads creation function for one or more SSH connections
create_threads(ip_reach(ip_list), ssh_connection)

#End of Program