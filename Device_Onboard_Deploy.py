
#!/usr/bin/env python3

#Import libraries
from datetime import datetime
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import getpass

#Capture admin pword
pword = getpass.getpass()

#Function to render config file for each host

#Device connect dictionary
def renderconfig(host,hname):
	device = {
		'device_type': 'cisco_nxos',
		'host': host,
		'username': 'admin',
		'password': pword,
	}
	#Connect do device and store commands to variables
	net_connect = ConnectHandler(**device)
	fname = f"{hname}.txt"
	net_connect.send_config_from_file(fname)
	net_connect.send_command("copy runs start")

#Read in hosts
with open("Device_Onboard_Hosts.txt") as f:
	lines = f.read().splitlines()

#Render config files for each host
for i in range(len(lines)):
	ev = eval(lines[i])
	renderconfig(ev["host"], ev["hname"])



