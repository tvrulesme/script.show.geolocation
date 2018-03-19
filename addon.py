import pyipinfoio
import xbmcgui
import xbmc
import xbmcaddon
from json import load
from urllib2 import urlopen
import subprocess
import pydevd
import os
#import resources.lib.kodisettings as settings
#import sys

def getVpnList():
	p = subprocess.Popen(["nmcli","con"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	outputText =  p.communicate()[0]
	for line in outputText.split('\n'):
		splitLine = line.split()
		if(splitLine and splitLine[2] == 'vpn'):
			if(splitLine[3] != '--'):
				vpnlistdisplay.append('[COLOR forestgreen]' + splitLine[0] + '[/COLOR] - Connected')
			else:
				vpnlistdisplay.append('[COLOR red]' + splitLine[0] + '[/COLOR] - Disconnected')
			vpnlist.append(splitLine[0])

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

vpnlistdisplay = [] 
vpnlist = [] 

# Set some global values.
_addonid = 'script.show.geolocation'

#image = _settings.get_path('icon.png')

#xbmc.translatePath('%s/%s' % (self.__path__, path))


__addon__       = xbmcaddon.Addon(id=_addonid)

print __addon__ 

#icon=os.path.join(addon.getAddonInfo('path'), 'resources','skins','Default','media', icon)


xbmc.executebuiltin('Notification(Title,A notification message,5000,' + __addon__ + ')')	




# my_ip = load(urlopen('http://jsonip.com'))['ip']
# ip = pyipinfoio.IPLookup()
# lookup = ip.lookup(my_ip)
# info = lookup['org'] 
# print('Current Geolocation Info', info)

#info = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']


getVpnList()

#print vpnlist

dialog = xbmcgui.Dialog()
selectedVpn = dialog.select('Select vpn',vpnlistdisplay)

if selectedVpn >= 0:
	password = ''
	connected = True if 'forestgreen' in vpnlistdisplay[selectedVpn] else False
	password = xbmcgui.Dialog().input('Enter password to disconnect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	
	if password:
		updown = 'down' if connected else 'up'
		print ( 'sudo -S nmcli con ' + updown +' id ' + vpnlist[selectedVpn] )
		process = subprocess.Popen('sudo -S nmcli con ' + updown +' id ' + vpnlist[selectedVpn] , shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + os.linesep)[1]
	




#print vpnlist[selectedVpn]


# if 'Virgin' not in info: 
# 	passDialog = xbmcgui.Dialog()
# 	password = passDialog.input('[COLOR forestgreen]' + info + '[/COLOR] enter password to disconnect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
# 	if password:
# 		process = subprocess.Popen('sudo -S nmcli con down id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
# 		process.communicate(password + '\n')[1]
# 		
# 		process = subprocess.Popen('sudo -S nmcli con down id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
# 
# else:	
# 	passDialog = xbmcgui.Dialog()
# 	password = passDialog.input('[COLOR red]' + info + '[/COLOR] enter password to connect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
# 	#print('#' + password + '#')
# 	if password:
# 		process = subprocess.Popen('sudo -S nmcli con up id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
# 		process.communicate(password + '\n')[1]


print 'done'