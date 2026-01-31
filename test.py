from pi5neo import Pi5Neo
from time import sleep
from picamzero import Camera

cam = Camera()
cam.start_preview()

neo = Pi5Neo('/dev/spidev0.0', 24, 800)

neo.fill_strip(255, 255, 255)
neo.update_strip()
sleep(100)

neo.fill_strip(0, 0, 0)
neo.update_strip()
cam.end_preview()