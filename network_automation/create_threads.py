from threading import Thread
import time

#Create threads
def create_threads(ip_list, function):

    threads = []

    for ip in ip_list:
        threadx = Thread(target = function, args = (ip,))
        threadx.start()
        time.sleep(.5)
        threads.append(threadx)

    for threadx in threads:
        threadx.join()    