#import xbmcaddon
#import xbmcgui
import os
import xbmc
import time
import threading
#import pydevd


global hasRun

def yesNoDialog():
		while not hasRun:
			if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
				print 'clicking yesnodialog'
				xbmc.executebuiltin('SendClick(11)')
			else:
				time.sleep(0.5)
				
def sendCommand(res):
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoscreen.resolution","value":'+res+'},"id":1}')

#pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

tempdir = xbmc.translatePath('special://temp/')
tempfile0 = os.path.join(tempdir, 'reslutiontoggle0')


hasRun = False

t1 = threading.Thread(target=yesNoDialog)
t1.start()

if not os.path.isfile(tempfile0):
	print 'Switching to full screen resolution'
	sendCommand('17')
	tempfile = open(tempfile0, "a")
	tempfile.close()
	
else:
	print 'Switching to projector resolution'
	sendCommand('20')
	os.remove(tempfile0)

hasRun = True	
t1.join(3)