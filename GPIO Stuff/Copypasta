from gpiozero import MotionSensor
from picamera import PiCamera
import datetime

pir = MotionSensor(4)
camera = PiCamera()
now = datetime.datetime.now()
filename = "intruder_" + str(now).replace(" ", "_") + ".h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	camera.stop_preview()
