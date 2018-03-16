import pyipinfoio
import xbmcgui
import pydevd
from json import load
from urllib2 import urlopen

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()

line1 = 'ORG: ' + (ip.lookup(my_ip))['org']
line2 = 'CITY: ' + (ip.lookup(my_ip))['city']
line3 = 'COUNTRY: ' +(ip.lookup(my_ip))['country']
line4 = 'REGION: ' +(ip.lookup(my_ip))['region']
line5 = 'HOST: ' +(ip.lookup(my_ip))['hostname']
line6 = 'IP: ' +(ip.lookup(my_ip))['ip']


xbmcgui.Dialog().textviewer('Current Geolocation Info', line1, line2, line3, line4, line5, line6)

#xbmcgui.Dialog().ok('Current Geolocation Info', line1, line2, line3, line4, line5, line6)

