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
        'username': 'admin',
        'password': 'Dubai123'
    }

    net_connect = ConnectHandler(**cisco_xe)
    output = net_connect.send_command_timing('install add file flash:cat9k_iosxe.16.09.01s.SPA.bin activate commit', delay_factor=300)
    if 'Press Quit(q) to exit, you may save configuration and re-enter the command. [y/n/q]' in output:
        output += net_connect.send_command_timing("y")  
    if 'This operation may require a reload of the system. Do you want to proceed? [y/n]' in output:
        output += net_connect.send_command_timing("y")
    print(output)
    print()
