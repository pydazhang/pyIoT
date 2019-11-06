import socket
import re
import time
import threading
import requests


def tanmu(rid, s):
    login_info = 'type@=loginreq/roomid@=%s/\0'%rid # sending login request
    info = login_info.encode('utf-8')  # transfer it into utf-8 as requested
    data_length = len(info) + 8
    value = 689  # the type of information for client sending to the server
    infohead = int.to_bytes(data_length, 4, 'little') + int.to_bytes(data_length, 4, 'little') \
    + int.to_bytes(value, 4, 'little')
    s.send(infohead + info)
    check=s.recv(1024)
    ch=re.compile(b'type@=(.+?)/userid')
    checknew = str(ch.findall(check))
    if checknew=='[b\'loginres\']':
        print('Connected to %s successfully'%rid)
    join_group = 'type@=joingroup/rid@=%s/gid@=-9999/\0'%rid# sending joingroup request
    info = join_group.encode('utf-8')  # transfer it into utf-8 as requested
    data_length = len(info) + 8
    value = 689  # the type of information for client sending to the server
    infohead = int.to_bytes(data_length, 4, 'little') + int.to_bytes(data_length, 4, 'little') \
    + int.to_bytes(value, 4, 'little')
    s.send(infohead + info)
#    while True:
#        data = s.recv(1024)
#       print(data)
 #      time.sleep(10)
    t0=time.time()
    while time.time()-t0<60:
        data = s.recv(1024)
        dm = re.compile(b'txt@=(.+?)/cid@')
        data_new = dm.findall(data)
        for i in range(0, len(data_new)):
            try:
                txt = data_new[0].decode(encoding='utf-8')
                print('%s:'%rid+txt)
            except AttributeError:
                print('Error')

def keep_alive(s):
    keeplive_info = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'  # heartbeat info
    info = keeplive_info.encode('utf-8')  # transfer it into utf-8 as requested
    data_length = len(info) + 8
    value = 689  # the type of information for client sending to the server
    infohead = int.to_bytes(data_length, 4, 'little') +int.to_bytes(data_length, 4, 'little') \
    + int.to_bytes(value, 4, 'little')
    while True:
        s.send(infohead + info)
        print('keeplive successfully\n')
        time.sleep(45)
        
def online():
    r = requests.get('https://www.douyu.com/gapi/rkc/directory/0_0/2')
    rold=re.compile('rid":(.+?),"rn')
    rnew=rold.findall(r.text)
    return rnew

def corehb():
    if __name__ == '__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # create a socket
        host = socket.gethostbyname("openbarrage.douyutv.com")  # get the host(8601) of Douyu
        port = 8601
        s.connect((host, port))        
        t = threading.Thread(target=keep_alive, args=(s,))
        t.start()
        
def core(rid):
    if __name__ == '__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # create a socket
        host = socket.gethostbyname("openbarrage.douyutv.com")  # get the host(8601) of Douyu
        port = 8601
        s.connect((host, port))        
        t = threading.Thread(target=tanmu, args=(rid, s))
        t.start()


rid=online()
print(rid)
corehb()
for i in rid[1:5]:
    core(i)
time.sleep(60)
for i in rid[6:10]:
    core(i)
