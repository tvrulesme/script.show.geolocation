import pyipinfoio
import xbmcgui
from json import load
from urllib2 import urlopen
import subprocess
#import pydevd

#pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()
lookup = ip.lookup(my_ip)

#info = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']
info = lookup['org'] 

print('Current Geolocation Info', info)

dialog = xbmcgui.Dialog()
if 'Virgin' not in info: 
	passDialog = xbmcgui.Dialog()
	password = passDialog.input('[COLOR forestgreen]' + info + '[/COLOR] enter password to disconnect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	if password:
		process = subprocess.Popen('sudo -S nmcli con down id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + '\n')[1]

else:	
	passDialog = xbmcgui.Dialog()
	password = passDialog.input('[COLOR red]' + info + '[/COLOR] enter password to connect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	#print('#' + password + '#')
	if password:
		process = subprocess.Popen('sudo -S nmcli con up id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + '\n')[1]


print 'done'