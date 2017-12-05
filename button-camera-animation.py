from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview()
#sleep(3)
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
