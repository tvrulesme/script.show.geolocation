import pyipinfoio
import subprocess
#import xbmcgui
import pydevd
import os

pydevd.settrace('192.168.0.55', stdoutToServer=True, stderrToServer=True)



openvpn = '/usr/sbin/openvpn'
workdir = os.path.dirname('/home/john/openvpn')
ip = '127.0.0.1'
port = 1337
ovpnconfig = 'ipvanish-UK-London-lon-a65.ovpn'
sudopwd = 'Penguin1'


#'sudo -S openvpn --daemon --management 127.0.0.1 1337 --config ~/openvpn/ipvanish-UK-London-lon-a65.ovpn'

#cmdline = '\'%s\' --cd \'%s\' --daemon --management %s %d --config \'%s\' ' % (
#            openvpn, workdir, ip, port, ovpnconfig)

#cmdline = 'echo \'%s\' | sudo -S %s' % (sudopwd, cmdline)
process = subprocess.Popen('sudo -S openvpn --daemon --management 127.0.0.1 1337 --config ~/openvpn/ipvanish-UK-London-lon-a65.ovpn', cwd=workdir, shell=True,
                                        stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

sudo_prompt = process.communicate('Penguin1' + '\n')[1]

print (process.pid)

