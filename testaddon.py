import pyipinfoio
import subprocess
#import xbmcgui
import pydevd
import os
from json import load
from urllib2 import urlopen

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()
lookup = ip.lookup(my_ip)

info = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']

#print('Current Geolocation Info', info)
print(info)

if 'Virgin' in info: 
	p = subprocess.Popen('sudo openvpn --config /home/john/openvpn/ipvanish-UK-London-lon-a48.conf', shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
	print(p.pid)
else:
	CREATE_NEW_PROCESS_GROUP = 0x00000200
	DETACHED_PROCESS = 0x00000008
	openvpn_cmd = ['sudo', 'killall', 'openvpn']
	p = subprocess.Popen('sudo killall openvpn', shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
	print(p.pid)


