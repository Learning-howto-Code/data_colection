from pi5neo import Pi5Neo
from time import sleep

neo = Pi5Neo('/dev/spidev0.0', 30, 250)

neo.fill_strip(255, 255, 255)
neo.update_strip()
sleep(5)

neo.fill_strip(0, 0, 0)
neo.update_strip()