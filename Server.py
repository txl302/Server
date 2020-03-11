import time

def vision():
	pass

def network_stream_rin():
	pass

def network_stream_woody():
	pass


if __name__ == "__main__":

    thre_v = threading.Thread(target = vision)

    thre_nsr = threading.Thread(target = network_stream_rin)
    thre_nsw = threading.Thread(target = network_stream_woody)


    thre_v.start()

    thre_nsr.start()
    thre_nsw.start()