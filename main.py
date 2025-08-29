from picamzero import Camera
from time import sleep
from pi5neo import Pi5Neo
import sys

SPI_DEVICE = '/dev/spidev0.0' # Rpi protocol to get the timing right for the GPIOs
SPI_SPEED_KHZ = 800 #speed of SPI protocol

neo = Pi5Neo(SPI_DEVICE, 30, SPI_SPEED_KHZ)

# Fill the strip with white (R,G,B = 255,255,255)

neo.fill_strip(255, 255, 255)
neo.update_strip()  # commit/send to LEDs
cam = Camera()
cam.start_preview()
# Keep the preview window open for
sleep(10)
