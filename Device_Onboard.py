#!/usr/bin/env python3

#Import libraries
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import getpass, yaml

#Capture admin pword
pword = getpass.getpass()

#Declare template variables
environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("Device_Template.jinja2")

with open('Device_Vars.yaml', 'r') as vars:
	lvars = yaml.safe_load(vars)

#peers = [{'peer': 'SPN201', 'peer_ip': '192.168.0.201'},{'peer': 'SPN202', 'peer_ip': '192.168.0.202'}]

output = template.render(lvars=lvars)
print(output)
