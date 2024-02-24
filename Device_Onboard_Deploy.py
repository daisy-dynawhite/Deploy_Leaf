
#!/usr/bin/env python3

#Import libraries
from datetime import datetime
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import getpass

#Capture admin pword
pword = getpass.getpass()

#Function to render host information to webpage

#Device connect dictionary
device = {
        'device_type': 'cisco_nxos',
        'host': '192.168.186.148',
        'username': 'admin',
        'password': 'daisy',
}

#Connect do device and store commands to variables
net_connect = ConnectHandler(**device)
net_connect.send_config_from_file("DAYZ-LFN104.txt")
