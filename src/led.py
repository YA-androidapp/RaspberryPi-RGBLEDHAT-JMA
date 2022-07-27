import time
from rpi_ws281x import PixelStrip, Color


LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_COUNT = 16        # Number of LED pixels.
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).


def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        while True:
            colorWipe(strip, Color(255, 0, 0))  # Red wipe

    except KeyboardInterrupt:
        pass
        ## colorWipe(strip, Color(0, 0, 0), 10)
