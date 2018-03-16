import pyipinfoio
import subprocess
import xbmcgui
import pydevd
from json import load
from urllib2 import urlopen

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()
lookup = ip.lookup(my_ip)

info = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']

print('Current Geolocation Info', info)


dialog = xbmcgui.Dialog()
if dialog.yesno('Current Geolocation Info', info,'Start VPN?'):
	print 'Going to start VPN'
else:
	print 'Not going to start VPN'


#openvpn_cmd = ['sudo', 'openvpn', '--config', 'client.cfg', '--auth-user-pass', 'hmaauth.conf']
#prog = subprocess.Popen(openvpn_cmd)

#prog.

#xbmcgui.Dialog().ok('Current Geolocation Info', 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname'])

