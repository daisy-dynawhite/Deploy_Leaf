#!/usr/bin/env python3

#Import libraries
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import getpass, yaml

#Capture admin pword
pword = getpass.getpass()

#Declare template variables
environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("Device_Onboard_Template.jinja2")

with open('Device_Onboard_Vars.yaml', 'r') as vars:
	lvars = yaml.safe_load(vars)

#Render config text via Jinja2 template
output = template.render(lvars=lvars)

#Save config to file
fname = lvars['hostname']+".txt"
with open (fname, mode="w", encoding="utf-8") as message:
	message.write(output)
