import getpass
import sys
import telnetlib
from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    cisco_xe = {
        'device_type': 'cisco_xe',
        'ip': ip_address_of_device,
        'username': 'ali.jaber',
        'password': 'Leen!2005Meel!2005'
    }

    net_connect = ConnectHandler(**cisco_xe)
    output = net_connect.send_config_set(commands_list)
    tn.read_until(b"Press Quit(q) to exit, you may save configuration and re-enter the command. [y/n/q] ")
    write(b"y")
    read_until(b"This operation may require a reload of the system. Do you want to proceed? [y/n] ")
    write(b"y\n")
    print (output)