import time
import board
import busio
import csv

# Voor nu van Adafruit binnenkort even zelf aanpassen
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create an I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
currentClamp = AnalogIn(ads, ADS.P0)
vibrationSensor = AnalogIn(ads, ADS.P1)

print("{:>5}\t{:>5}\t{:>5}\t{:>5}".format("raw A0", "v A0", "raw A1", "v A1"))

while True:
    print("{:>5}\t{:>5.3f}\t{:>5}\t{:>5.3f}".format(currentClamp.value, currentClamp.voltage, vibrationSensor.value, vibrationSensor.voltage))
    time.sleep(0.2)




