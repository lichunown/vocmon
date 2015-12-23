class transpotstring12345:  #have some problem  
    def __init__(self,string):
        self.data=[]
        name=''
        value=''
        dirc={}
        isname=True
        for char in string:
            if char==',':
                isname=False
                continue
            if char==';':
                isname=True
                dirc={name:value}
                self.data.append(dirc)
                name=''
                value=''
                continue
            if isname:
                name+=char
            else:
                value+=char
        
    def getchar(self,num):
        return self.data[num]
    def printall(self):
        print self.data
    def getValueByName(self,name):
        pass
#a=transpotstring("dsvfs,hf;sdvs,gfgbd;aszfcse,fcgbd;fasdc,fcch;")
#a.printall()
 #print a.getchar(0)   
############################################################

class transoptstring:
    def __init__(self,string):        
        self.data={}
        name=''
        value=''
        isname=True
        for char in string:
            if char==':':
                isname=False
                continue
            if char==';':
                isname=True
                self.data[name]=value
                name=''
                value=''
                continue
            if isname:
                name+=char
            else:
                value+=char

    def printall(self):
        print self.data
    def getValueByName(self,name):
        return self.data[name]

def transpot(string):
    data={}
    name=''
    value=''
    isname=True
    for char in string:
        if char==':':
            isname=False
            continue
        if char==';':
            isname=True
            data[name]=value
            name=''
            value=''
            continue
        if isname:
            name+=char
        else:
            value+=char
    return data

    
def getalldata(sock):
    returndata=''
    while True:        
        data=sock.recv(1024)       
        if not len(data):
            break
        returndata+=data
    return returndata
class User:
    def __init__(self):
        self.username=''
        self.password=''
        self.addr=('0.0.0.0',0)