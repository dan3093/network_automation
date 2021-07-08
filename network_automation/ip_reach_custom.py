import sys
import subprocess
import platform
from multiping import MultiPing
from multiping import multi_ping

#Check IP reachability
def ip_reach(list_of_ip_addresses):

    #set ip addresses to test
    mp = MultiPing([item.rstrip("\n") for item in list_of_ip_addresses])

    #send ping to ip addresses
    mp.send()

    #received responses within .1 seconds
    responses, no_responses = mp.receive(3)

    ip_list_good = []

    #print out addressses that responded
    for response, time in responses.items():
        print(f"\n{response} has responded in {time} seconds.\n")
        ip_list_good.append(response)
        

    #print out addressses that did not respond
    for no_response in no_responses:
        print(f"\n{no_response} has failed to respond, please check connection and try again.\n")

    return(ip_list_good)
    
