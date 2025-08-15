from pi5neo import Pi5Neo
import time
import sys

NUM_LEDS = 30
SPI_DEVICE = '/dev/spidev0.0'
SPI_SPEED_KHZ = 800  # pass as kHz (example from README)

# Init
neo = Pi5Neo(SPI_DEVICE, NUM_LEDS, SPI_SPEED_KHZ)
print("Opened SPI device:", SPI_DEVICE)

try:
    while True:
        for i in range(NUM_LEDS):
            # Turn everything off, set one LED to purple, then push to strip
            neo.clear_strip()
            neo.set_led_color(i, 150, 0, 90)   # set index i to purple (R,G,B)
            neo.update_strip()                 # commit/send to LEDs
            time.sleep(0.02)
except KeyboardInterrupt:
    # clean shutdown: turn off LEDs
    neo.clear_strip()
    neo.update_strip()
    print("\nExiting and cleared strip.")
    sys.exit(0)

