import netmiko
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.102.5',
    port = 22,
    username = 'admin',
    password = 'pass'
)
output = sshCli.send_command("show ip int brief")
print("{}\n".format(output))
config_commands = [
    'int loopback 1',
    'ip add 10.1.1.1 255.255.255.0',
    'desc PYTHONNETMIKO\'s loopback1',
    'int loopback 2',
    'ip add 10.2.2.2 255.255.255.0',
    'desc PYTHONNETMIKO\'s loopback2'
]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))
output = sshCli.send_command("show ip int brief")
print("{}\n".format(output))
