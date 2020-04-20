import socket

import json

#communication with Rin
sr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#communication with Woody
sw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


Woody = ('192.168.1.156', 9902)
Rin = ("192.168.1.80", 9902)

server_ip = '192.168.1.83'

server_rin_port = 9901
server_woody_port = 9902

server_rin = (server_ip, server_rin_port)
server_woody = (server_ip, server_woody_port)

sr.bind(server_rin)
sw.bind(server_woody)
 
def get_local_ip():
    try:
        s_t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_t.connect(('8.8.8.8', 80))
        ip = s_t.getsockname()[0]
    finally:
        s_t.close()

    return ip

# def sendto(data):
#     data = json.dumps(data)
#     #data.encode()
#     s.sendto(data.encode(), Woody)

# def rece():
#     raw_data,addr = s.recvfrom(64000)
#     data = json.loads(raw_data.decode())
#     return data

def recefrom_rin_img():
	data, addr = sr.recvfrom(64000)
	return data

def recefrom_woody_img():
    data, addr = sw.recvfrom(64000)
    return data



def recefrom_woody_data():
    raw_data,addr = sw.recvfrom(64000)
    data = json.loads(raw_data.decode())
    return data


if __name__ == '__main__':
	print(get_local_ip())
