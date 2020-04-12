
import getpass
import sys
import telnetlib
from netmiko import ConnectHandler

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
    output = net_connect.send_command('show ip interface brief')
    print (output)