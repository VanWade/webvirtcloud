import guestfs

# GuestFS
gfs = guestfs.GuestFS(python_return_dict=True)
gfs.add_domain('zntest_templat')
gfs.launch()
print(gfs.list_filesystems())
print(gfs.inspect_os())
print(gfs.inspect_get_mountpoints('/dev/cl_centos73-1611/root'))
gfs.mount('/dev/cl_centos73-1611/root', '/')
# parts = gfs.list_partitions()
# print(parts)
# gfs.mount(parts[1], '/')
print(gfs.ls('/'))
print(gfs.ls('/etc/sysconfig/network-scripts/'))
print(gfs.cat('/etc/sysconfig/network-scripts/ifcfg-eth0'))
print(gfs.cat('/etc/resolv.conf'))
"""
TYPE=Ethernet
BOOTPROTO=static
IPADDR={}
PREFIX=20
GATEWAY=192.168.16.1
DNS1=192.168.1.11
DNS2=114.114.114.114
NAME="eth0"
DEVICE="eth0"
ONBOOT="yes"
"""
