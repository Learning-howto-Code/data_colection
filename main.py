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
    
    neo.fill_strip(200, 200, 200) #sets LED's to white and a little dimmer
    neo.update_strip()
    print("light on")
    picam2 = Picamera2()
    config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
    picam2.configure(config)
    picam2.start()
    print("activated cam")
    sleep(2)
    print("waited 2 sec")

    try:
        while True:
            filename = f"{img_folder}/img_{strftime('%Y%m%d_%H%M%S_%f')}.jpg"   #names pic as timestamp
            picam2.capture_file(filename)
            print("took pic")
            sleep(.2)
    
    finally:
        picam2.close()
        del picam2 #stops worker funtion
        print("stopped cam")
        neo.fill_strip(0, 0, 0)
        neo.update_strip()
        print("turned off light")

take_pic()
