from picamzero import Camera
from time import sleep, strftime
from pi5neo import Pi5Neo

img_folder= "/home/jake/Downloads/data_collection/images"


SPI_DEVICE = '/dev/spidev0.0' # Rpi protocol to get the timing right for the GPIOs
SPI_SPEED_KHZ = 800 #speed of SPI protocol

pin = 30
neo = Pi5Neo(SPI_DEVICE, pin, SPI_SPEED_KHZ)

def take_pic():
    filename = f"{img_folder}/img_{strftime('%Y%m%d_%H%M%S')}.jpg"
    neo.fill_strip(200, 200, 200) #sets color to pure white
    neo.update_strip()  #sends command
    cam = Camera()
    cam.take_photo(filename)
    neo.fill_strip(0, 0, 0) #sets LED's to black

take_pic()
