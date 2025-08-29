from picamzero import Camera
from time import sleep
from pi5neo import Pi5Neo
from time import strftime

img_folder= "/home/jake/Downloads/data_collection/images"
filename = f"{img_folder}/img_{strftime('%Y%m%d_%H%M%S')}.jpg"

SPI_DEVICE = '/dev/spidev0.0' # Rpi protocol to get the timing right for the GPIOs
SPI_SPEED_KHZ = 800 #speed of SPI protocol

pin = 30
neo = Pi5Neo(SPI_DEVICE, pin, SPI_SPEED_KHZ)

def take_pic():

    neo.fill_strip(255, 255, 255) #sets color to pure white
    neo.update_strip()  #sends command
    cam = Camera()
    cam.take_photo(filename)
    neo.fill_strip(0, 0, 0) #sets LED's to black

take_pic()
