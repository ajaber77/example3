
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
    output = net_connect.send_command_timing('install add file flash:cat9k_iosxe.16.12.02t.SPA.bin activate commit')
    if 'This operation may require a reload of the system. Do you want to proceed? [y/n]' in output:
    output += net_connect.send_command_timing("y")
    print(output)
    