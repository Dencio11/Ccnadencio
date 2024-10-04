import json
import netmiko
from netmiko import ConnectHandler

#tell python to open the json file:
with open ('config1.json') as config_file:
    config = json.load(config_file)
    
    #Extract json config to python memory:
    device_info = config['device']
    interface_config = config ['inerface_config']
    new_hostname = config['new_hostname']
    
    #talk using ssh to cisco
    net_connect = ConnectHandler(**device_info)
    
    #start configuring cia enable
    net_connect.enable
    
    #build the cisco configuration via json:
    command = [
        f"interface{interface_config['interface']}",
        f"ip address{interface_config['new_ip']} {interface_config['subnet_mask']}",
        "no shutdown",
        "exit",
        f"hostname{new_hostname}"
    ]  
        
#send config to cisco device:
output = net_connect.send_config_set(command)    
print(output)
        
#exit/logout from Cisco:
net_connect.disconnect
        