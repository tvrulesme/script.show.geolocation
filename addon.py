import pyipinfoio
import xbmcgui
import xbmc
import xbmcaddon
from json import load
from urllib2 import urlopen
import subprocess
#import pydevd
import os

green = '[COLOR forestgreen]'
red = '[COLOR red]'
endColor = '[/COLOR]'
#vpnConnected = False


def getVpnList():
	p = subprocess.Popen(["nmcli","con"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	outputText =  p.communicate()[0]
	vpnConnected = False
	for line in outputText.split('\n'):
		splitLine = line.split()
		if(splitLine and splitLine[2] == 'vpn'):
			if(splitLine[3] != '--'):
				vpnlistdisplay.append(green + splitLine[0] + endColor + ' - Connected')
				vpnConnected = True
			else:
				vpnlistdisplay.append(red + splitLine[0] + endColor + ' - Disconnected')
			vpnlist.append(splitLine[0])
	return vpnConnected

			
def showVpnInfo(connected):
	iconpath = xbmcaddon.Addon().getAddonInfo('path').decode("utf-8") + "/icon.png"
	my_ip = load(urlopen('http://jsonip.com'))['ip']
	ip = pyipinfoio.IPLookup()
	lookup = ip.lookup(my_ip)
	#message = 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname']
	org = lookup['org']
	message = green + org + endColor if connected else red + org + endColor
	header = 'Connected to VPN' if connected else 'Disconnected from VPN'
	xbmc.executebuiltin('Notification(' + header + ',' + message + ',5000,' + iconpath+ ')')

#pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

vpnlistdisplay = [] 
vpnlist = [] 

connected = getVpnList()

dialog = xbmcgui.Dialog()
selectedVpn = dialog.select('Select vpn',vpnlistdisplay)

if selectedVpn >= 0:
	password = ''
	connectDisconnect = 'disconnect' if connected else 'connect'
	password = xbmcgui.Dialog().input('Enter password to disconnect VPN', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	
	if password:
		updown = 'down' if connected else 'up'
		print ( 'sudo -S nmcli con ' + updown +' id ' + vpnlist[selectedVpn] )
		process = subprocess.Popen('sudo -S nmcli con ' + updown +' id ' + vpnlist[selectedVpn] , shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate(password + os.linesep)[1]
	

connected = getVpnList()

showVpnInfo(connected)

print 'done'