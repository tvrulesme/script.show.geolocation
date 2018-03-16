import pyipinfoio
import subprocess
import xbmcgui
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

dialog = xbmcgui.Dialog()
if 'Virgin' not in info: 
	if dialog.yesno('VPN connected', info,'Stop VPN?'):
		print 'Going to stop VPN'
		CREATE_NEW_PROCESS_GROUP = 0x00000200
		DETACHED_PROCESS = 0x00000008
		openvpn_cmd = ['sudo', 'killall', 'openvpn']
		p = subprocess.Popen('sudo killall openvpn', shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
		print(p.pid)
	else:
		print 'Not going to stop VPN'
else:	
	if dialog.yesno('VPN not connected', info,'Start VPN?'):
		print 'Going to start VPN'
		CREATE_NEW_PROCESS_GROUP = 0x00000200
		DETACHED_PROCESS = 0x00000008
		#openvpn_cmd = ['nohup','sudo', 'openvpn', '--config', 'home/john/openvpn/ipvanish-UK-London-lon-a48.conf' ]
		p = subprocess.Popen('sudo openvpn --config /home/john/openvpn/ipvanish-UK-London-lon-a48.conf', shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
		
		
		#p = subprocess.Popen(openvpn_cmd , shell=True, stdout=None, stderr=None, preexec_fn=os.setpgrp)
		print(p.pid)
	else:
		print 'Not going to start VPN'






#openvpn_cmd = ['sudo', 'openvpn', '--config', 'client.cfg', '--auth-user-pass', 'hmaauth.conf']
#prog = subprocess.Popen(openvpn_cmd)

#prog.

#xbmcgui.Dialog().ok('Current Geolocation Info', 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname'])

