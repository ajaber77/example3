import getpass
import sys
import telnetlib
from netmiko import ConnectHandler


cisco_xe = {
        'device_type': 'cisco_xe',
        'ip': '10.113.83.10',
        'username': 'admin',
        'password': 'Dubai123'
}

net_connect = ConnectHandler(**cisco_xe)
output = net_connect.send_command('show version')

Version = output.index('Version')

print(output[Version: Version + 18])




