from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time

from multiprocessing.dummy import Pool as ThreadPool

#------------------------------------------------------------------------------
def read_devices( devices_filename ):

    devices = {}  # create our dictionary for storing devices and their info

    with open( devices_filename ) as devices_file:

        for device_line in devices_file:

            device_info = device_line.strip().split(',')  #extract device info from line

            device = {'ipaddr':   device_info[0]}  # create dictionary of device objects ...

            devices[device['ipaddr']] = device  # store our device in the devices dictionary
                                                # note the key for devices dictionary entries is ipaddr

    print ('\n----- devices --------------------------')
    pprint( devices )

    return devices
    
 #------------------------------------------------------------------------------
def config_worker( device ):

    #---- Connect to the device
    session = ConnectHandler( device_type='cisco_xe', ip=device['ipaddr'], username='admin', password='Dubai123')

    #---- Use CLI command to get configuration data from device
    print ('---- Getting configuration from device' + device['ipaddr'])
    config_data = session.send_command('show run')
   
    #---- Write out configuration information to file
    config_filename = 'config-' + device['ipaddr']  # Important - create unique configuration file name

    print ('---- Writing configuration: ', config_filename)
    with open( config_filename, 'w' ) as config_out:  config_out.write( config_data )

    session.disconnect()

    return

#==============================================================================
# ---- Main: Get Configuration
#==============================================================================
devices = read_devices( 'devices-file' )

num_threads_str = input( '\nNumber of threads (5): ' ) or '5'
num_threads     = int( num_threads_str )

#---- Create list for passing to config worker
config_params_list = []
for ipaddr,device in devices.items():
   config_params_list.append( ( device ) )
   

starting_time = time()

print ('\n--- Creating threadpool, launching get config threads\n')
threads = ThreadPool( num_threads )
results = threads.map( config_worker, config_params_list )

threads.close()
threads.join()

print ('\n---- End get config threadpool, elapsed time=', time()-starting_time)



