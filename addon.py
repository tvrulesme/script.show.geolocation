import pyipinfoio
import xbmcgui
import pydevd
from json import load
from urllib2 import urlopen

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)

my_ip = load(urlopen('http://jsonip.com'))['ip']
ip = pyipinfoio.IPLookup()

line1 = 'ORG: ' + (ip.lookup(my_ip))['org']
print(ip.lookup(my_ip))['city']
print(ip.lookup(my_ip))['country']
print(ip.lookup(my_ip))['region']
print(ip.lookup(my_ip))['hostname']
print(ip.lookup(my_ip))['ip']


xbmcgui.Dialog().ok('Current Geolocation Info', line1)

