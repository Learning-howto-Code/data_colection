from picamera2 import Picamera2
from time import sleep, strftime
from pi5neo import Pi5Neo
import os

# Image folder
img_folder = "/home/jake/Downloads/data_collection/images"
os.makedirs(img_folder, exist_ok=True)  # make sure folder exists

# SPI setup for NeoPixel
SPI_DEVICE = '/dev/spidev0.0'
SPI_SPEED_KHZ = 800
pin = 30
neo = Pi5Neo(SPI_DEVICE, pin, SPI_SPEED_KHZ)

def take_pic():
    # Generate timestamped filename
    filename = f"{img_folder}/img_{strftime('%Y%m%d_%H%M%S')}.jpg"

    # Turn LEDs white
    neo.fill_strip(200, 200, 200)
    neo.update_strip()

    # Initialize Picamera2
    picam2 = Picamera2()
    picam2.start_preview()          # optional, shows preview if running desktop
    sleep(1)                        # allow camera to adjust exposure/white balance

    picam2.capture_file(filename)   # capture image

    picam2.stop_preview()           # stop preview
    del picam2                      # release camera

    # Turn LEDs off
    neo.fill_strip(0, 0, 0)
    neo.update_strip()

take_pic()
