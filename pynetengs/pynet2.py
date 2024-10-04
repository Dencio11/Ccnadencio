import json
import netmiko
from netmiko import ConnectHandler

#tell python to open the Json file:
with open('config1a.json') as config_file:
    config = json.load(config_file)
 
 #Extract json config to python memory:
device_info = config['device']
interface_config1 = config['interface_config1']
interface_config2 = config['interface_config2']
new_hostname = config['new_hostname']
 
 #Talk using ssh to cisco:
net_connect = ConnectHandler(**device_info)
 
 #start configuring via enable
net_connect.enable
 
 #build the Cisco configuration Via JSON:
commands = [
     f"interface {interface_config1['interface']}",
     f"ip address {interface_config1['new_ip']} {interface_config1['subnet_mask']}",
     "no shutdown",
     "exit",
     f"interface {interface_config2['interface']}",
     f"ip address {interface_config2['new_ip']} {interface_config2['subnet_mask']}",
     "no shutdown",
     "exit",
     f"hostname {new_hostname}"
 ]

#send config to cisco device:
output = net_connect.send_config_set(commands)
print(output)

#exit/logout from Cisco:
net_connect.disconnect

