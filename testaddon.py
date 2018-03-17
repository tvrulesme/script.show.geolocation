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


p = subprocess.Popen('sudo openvpn --config /home/john/openvpn/ipvanish-UK-London-lon-a48.conf', shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
print(p.pid)


