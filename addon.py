import pyipinfoio
import xbmcgui
from json import load
from urllib2 import urlopen
import subprocess
import pydevd

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()
lookup = ip.lookup(my_ip)
info = lookup['org'] 
print('Current Geolocation Info', info)

#info = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']

vpnlist = [] 

p = subprocess.Popen(["nmcli","con"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
outputText =  p.communicate()[0]
for line in outputText.split('\n'):
	splitLine = line.split()
	if(splitLine and splitLine[2] == 'vpn'):
		vpnlist.append(splitLine[0])

print vpnlist

dialog = xbmcgui.Dialog()
if 'Virgin' not in info: 
	passDialog = xbmcgui.Dialog()
	password = passDialog.input('[COLOR forestgreen]' + info + '[/COLOR] enter password to disconnect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	if password:
		process = subprocess.Popen('sudo -S nmcli con down id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + '\n')[1]
		
		process = subprocess.Popen('sudo -S nmcli con down id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

else:	
	passDialog = xbmcgui.Dialog()
	password = passDialog.input('[COLOR red]' + info + '[/COLOR] enter password to connect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	#print('#' + password + '#')
	if password:
		process = subprocess.Popen('sudo -S nmcli con up id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + '\n')[1]


print 'done'