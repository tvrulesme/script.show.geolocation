import pyipinfoio
#import subprocess
import xbmcgui
import pydevd
#import os
from json import load
from urllib2 import urlopen
import xbmc

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
		xbmc.executebuiltin('XBMC.RunScript(script.openvpn,disconnect)')
	else:
		print 'Not going to stop VPN'
else:	
	if dialog.yesno('VPN not connected', info,'Start VPN?'):
		print 'Going to start VPN'
		xbmc.executebuiltin('XBMC.RunScript(script.openvpn,ipvanish)')
	else:
		print 'Not going to start VPN'






#openvpn_cmd = ['sudo', 'openvpn', '--config', 'client.cfg', '--auth-user-pass', 'hmaauth.conf']
#prog = subprocess.Popen(openvpn_cmd)

#prog.

#xbmcgui.Dialog().ok('Current Geolocation Info', 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname'])

