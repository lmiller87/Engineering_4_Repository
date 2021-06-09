import time
import picamera
frame = 1

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	while True:
		i = str(input("Click enter to take a frame or x then enter to exit: "))# prompts user input
		try:
			if i == "":# if they only click enter then it will run this
				camera.capture('/home/pi/Documents/Engineering_4_Notebook/Pictures/animation/frame%03d.jpg' % frame)# this captures a picture with a changing frame
				frame += 1# increases frame for the next picture
			elif i == "x":# if they enter x and enter then it will run this code to end the loop
				camera.stop_preview()
				break
		except KeyboardInterrupt:# also if there is a keyboard interrupt it does the same thing as the elif
			camera.stop_preview()
			break
