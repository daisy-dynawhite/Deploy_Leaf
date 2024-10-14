<div align='center'>

<h1>Nexus 9K - Automated Device Deployment</h1>
<h4> <span> · </span> <a href="https://github.com/daisy-dynawhite/Deploy_Leaf/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/daisy-dynawhite/Deploy_Leaf/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/daisy-dynawhite/Deploy_Leaf/issues"> Request Feature </a> </h4>
</div>

# :star2: About the Project
- <p>This project is designed to automate the configuration deployment of Cisco Nexus 9K devices operating within VXLAN BGP EVPN solutions.</p>
- <p>In this example, BUM traffic is handled by PIM with an anycast RP on the spines and a discrete multicast group per L2VNI</p>
- <p>The structure of the project is designed to be extensible, e.g., adding L3VNI to the Jinja2 template / YAML vars</p>
- <p>The Device Onboard Config python script loads N9K vars from a YAML file and renders a txt file with the corresponding configuration</p>
- <p>The Device Onboard Deploy python script reads in hosts vars and the config file created in the previous step and pushes via Netmiko to the targeted device</p>

## :dart: Languages
- Python3, Jinja2 and YAML.
