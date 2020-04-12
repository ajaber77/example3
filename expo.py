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
    iosxe_device = {
        'device_type': 'cisco_iosxe',
        'ip': ip_address_of_device,
        'username': 'alijabe',
        'password': 'Leen!2005Meel!2005'
    }

    net_connect = ConnectHandler(**iosxe_device)
    output = net_connect.send_config_set(commands_list)
    tn.read_until(b"This operation may require a reload of the system. Do you want to proceed? [y/n] ")
    tn.write(b"y\n")
    print (output)