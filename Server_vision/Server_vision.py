import cv2

face_cascade = cv2.CascadeClassifier('Server_vision/haarcascade_frontalface_alt.xml')

def vision():
	pass


def main():
	
	rectangleColor = (0,165,255)  

	cap = cv2.VideoCapture(0)
	res_w = 320
	res_h = 240
	cap.set(3,res_w);
	cap.set(4,res_h);

	while True:
		ret, img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		maxArea = 0
		x = 0
		y = 0
		w = 0  
		h = 0

		for (_x,_y,_w,_h) in faces:
		    if _w*_h > maxArea:
		        x = _x
		        y = _y
		        w = _w
		        h = _h
		        maxArea = w*h
		if maxArea > 0:
		    cv2.rectangle(img,(x,y),(x+w,y+h),rectangleColor,4)
		    a = x+w/2 - res_w/2
		    b = y+h/2 - res_h/2

		    flag_s = 1

		cv2.imshow('img',img)
		k = cv2.waitKey(20) & 0xff
		if k == 27:
		    break


if __name__ == '__main__':
	main()