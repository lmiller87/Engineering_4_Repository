import time
import picamera

print("Picture 1")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'colorswap' 
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test1.jpg')

print("Done")

print("Picture 2")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'pastel'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test2.jpg')

print("Done")

print("Picture 3")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'gpen'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test3.jpg')

print("Done")

print("Picture 4")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'solarize'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test4.jpg')

print("Done")

print("Picture 5")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'cartoon'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test5.jpg')

print("Done")
