import pyipinfoio
import xbmcgui
#import pydevd
from json import load
from urllib2 import urlopen

#pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()
lookup = ip.lookup(my_ip)

line1 = 'ORG: ' + lookup['org']
line2 = 'CITY: ' + lookup['city']
#line3 = 'COUNTRY: ' +(ip.lookup(my_ip))['country']
line4 = 'REGION: ' +lookup['region']
line5 = 'HOST: ' +lookup['hostname']
#line6 = 'IP: ' +(ip.lookup(my_ip))['ip']


#xbmcgui.Dialog().ok('Current Geolocation Info', line1+'\n'+ line2+'\n'+  line3+'\n'+  line4+'\n'+  line5+'\n'+  line6)

xbmcgui.Dialog().ok('Current Geolocation Info', line1+'\n'+ line2+'\n'+   line4+'\n'+  line5)

#xbmcgui.Dialog().ok('Current Geolocation Info', line1, line2, line3, line4, line5, line6)

