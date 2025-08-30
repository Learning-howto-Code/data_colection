from picamera2 import Picamera2
from time import sleep, strftime
from pi5neo import Pi5Neo
import os

# Image folder
img_folder = "/home/jake/Downloads/data_collection/images"

# SPI setup for NeoPixel
SPI_DEVICE = '/dev/spidev0.0'
SPI_SPEED_KHZ = 800
pin = 30
neo = Pi5Neo(SPI_DEVICE, pin, SPI_SPEED_KHZ)

def take_pic():
    filename = f"{img_folder}/img_{strftime('%Y%m%d_%H%M%S')}.jpg" #names pic as timestamp
    neo.fill_strip(200, 200, 200) #sets LED's to white and a little dimmer
    neo.update_strip()
    picam2 = Picamera2()
    sleep(1)  #waits for cam to calibrate
    picam2.capture_file(filename) 
    picam2.close()
    del picam2 #stops worker funtion
    neo.fill_strip(0, 0, 0)
    neo.update_strip()

take_pic()
