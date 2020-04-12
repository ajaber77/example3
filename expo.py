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
    cmd = 'do install add file flash:cat9k_iosxe.16.12.02t.SPA.bin activate commit'
    output = net_connect.send_command(
    cmd, 
    expect_string=r'Press Quit(q) to exit, you may save configuration and re-enter the command. [y/n/q] '
    )
    output += net_connect.send_command('y')
    print (output)