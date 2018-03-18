import pyipinfoio
#import subprocess
import xbmcgui
import pydevd
#import os
from json import load
from urllib2 import urlopen
import xbmc
import subprocess

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
		#passDialog = xbmcgui.Dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
		passDialog = xbmcgui.Dialog()
		password = passDialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
		
		
		#d = passDialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
		print(password)
		
		process = subprocess.Popen('sudo -S nmcli con up id ipvanish-UK-London-lon-a48', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

		sudo_prompt = process.communicate(password + '\n')[1]
		
		
		
		#sudo nmcli con down id ipvanish-UK-London-lon-a48
		
		#RunScript(script.openvpn, disconnect)
		xbmc.executebuiltin('XBMC.RunScript(script.openvpn,ipvanish)')
	else:
		print 'Not going to start VPN'


print 'done'



#openvpn_cmd = ['sudo', 'openvpn', '--config', 'client.cfg', '--auth-user-pass', 'hmaauth.conf']
#prog = subprocess.Popen(openvpn_cmd)

#prog.

#xbmcgui.Dialog().ok('Current Geolocation Info', 'ORG: ' + lookup['org'] +'\n'+ 'CITY: ' + lookup['city']+'\n'+   'REGION: ' +lookup['region']+'\n'+  'HOST: ' +lookup['hostname'])

