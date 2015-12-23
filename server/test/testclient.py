import socket
import threading
from time import sleep
from string.stringchange import transpot,getalldata

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host="127.0.0.1"
port=9000

s.connect((host,port))
username=raw_input("username:")
data="type:login;username:"+username+";password:123;"
s.sendall(data)
print "log in return : %s" % s.recv(1024)
while True:
	data=raw_input("in:")
	if data=='getalluser':
		data="type:getalluser;"
	if data=='exit':
		s.close()
		break
	s.sendall(data)
	print 'have send %s' % data
	#print getalldata(s)
	print 'receive: %s' % s.recv(1024)