from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview()
#sleep(3)
button.wait_for_press()
camera.capture('/home/pi/image3.jpg')
camera.stop_preview()
