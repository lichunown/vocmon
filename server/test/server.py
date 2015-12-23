#coding:utf-8

import socket
import threading
from time import sleep
from string.stringchange import transpot,getalldata,User



host=""
port=9000

connectuser=[]
L=threading.Lock()

def connecting(sock,addr):
    
    print 'receive from %s' % addr[0]
    while True:
        try:
            data=sock.recv(1024)
        except socket.error,e:
            if L.acquire():
                global connectuser
                connectuser.remove(user)
                L.release()
            print "%s have something wrong." % user.username 
            break
        print 'receive data=%s' % data.__str__()
        datadir=transpot(data)
        print datadir

        if datadir['type']=='login':
            #checking user name
            #if not true 
            #sendall("password wrong")
            #end socket
            #else
            user=User()
            user.username=datadir['username']
            user.password=datadir['password']
            user.addr=addr
            if L.acquire():
                global connectuser               
                connectuser.append(user)
                L.release()
                print connectuser
            sock.sendall("name:lcy;level:99;")
        if datadir['type']=='get':
            #this need add limit
            sendstring=''
            if L.acquire():
                sendstring=''
                global connectuser
                if datadir['valuename']=='alluser':
                    for tempuser in connectuser:
                        sendstring+=tempuser.username+';'
                if datadir['valuename']=='userip'
                L.release()
            sock.sendall(sendstring)

    
    sock.close()
    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(50)
while True:
    sleep(0.1)
    sock,addr=s.accept()
    t=threading.Thread(target=connecting,args=(sock,addr))
    t.setDaemon(True)#保证主进程结束子进程也结束
    t.start()

