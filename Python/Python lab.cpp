*SITE1*
conf t
hostname SITE1
no ip domain-lookup
int f0/0
no shut
ip add 172.16.10.2 255.255.255.0
exit

int lo0
no shut
ip add 1.1.1.1 255.255.255.255
end
wr

