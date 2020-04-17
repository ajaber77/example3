
# this is a base script to generate muliple configuration files
# devices_details = switch1_hostname, 192.168.1.1       switch2_hostname, 192.168.1.2
# commands_file = 
# Hostname Hostaname1
#!
#Interface Ethernet0
#ip address address1 255.255.255.0

with open('devices_details') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    device_info = devices.strip().split(',')
    device = {
        'hostname': device_info[0],
        'ipaddr1': device_info[1]       
    }

    with open('commands_file') as f:
        output = f.read()

        SW_output = output.replace("address1",device_info[1]).replace("Hostaname1", device_info[0])

        config_filename =  device_info[0]  # Important - create unique configuration file name

        print ('---- Generating configuration for : ', config_filename)

        with open( config_filename, 'w' ) as config_out:  config_out.write( SW_output )

    
