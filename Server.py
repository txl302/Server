import cv2

import time
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import threading

from Server_network import Server_network as Sn
from Server_vision import Server_vision as Sv

import random as rd

def vision():
	pass

def network_stream_rin():
	pass

def network_stream_woody():
	pass

def main():
	thre_v = threading.Thread(target = vision)
	thre_nsr = threading.Thread(target = network_stream_rin)
	thre_nsw = threading.Thread(target = network_stream_woody)

	thre_v.start()
	thre_nsr.start()
	thre_nsw.start()


def Rin():
	global pro_rin_sight

	time.sleep(1)

	while True:
		str_encode = Sn.recefrom_rin_img()
		nparr = np.fromstring(str_encode,np.uint8)
		Rin_sight = cv2.imdecode(nparr, 1)

		pro_rin_sight, loc = Sv.face_detect(Rin_sight)

		print(loc)

def Woody():
	global Woody_sight

	while True:
		str_encode = Sn.recefrom_woody_img()
		nparr = np.fromstring(str_encode,np.uint8)
		Woody_sight = cv2.imdecode(nparr, 1)

def Rin_data():
	pass

def Woody_data():
	pass

def monitor():
	while True:
		cv2.imshow('Rin_sight_moni', pro_rin_sight)
		cv2.imshow('Woody_sight_moni', Woody_sight)
		cv2.waitKey(50)

def update(frame):
	global dis
	global dis2
	global line

	a = frame
	time.sleep(np.random.rand()/10)
	dis[0:-1] = dis2[1:]
	dis[-1] = a
	dis2 = dis

	line.set_ydata(dis)

	plt.setp(line)
	return line

def animation():
	data = []
	dis = np.zeros(40)
	dis2 = dis
	fig, ax = plt.subplots()
	line, = ax.plot(dis)
	ax.set_ylim(0,100)
	plt.grid(True)

	ani = animation.FuncAnimation(fig, update, frames = data, interval = 10)
	plt.show()

	

def main_test():

	thre_rin = threading.Thread(target = Rin)
	thre_woody = threading.Thread(target = Woody)

	thre_moni = threading.Thread(target = monitor)

	thre_rin.start()
	thre_woody.start()

	time.sleep(3)

	thre_moni.start()


if __name__ == "__main__":
	animation()
