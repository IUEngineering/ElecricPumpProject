import board
import busio
import csv
import time

# Voor nu van Adafruit binnenkort even zelf aanpassen
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# open the file in the write mode
f = open('/mnt/data/testing/test', 'w')

# create the csv writer
writer = csv.writer(f)

# Create an I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADC object using the I2C bus
ads = ADS.ADS1015(i2c, data_rate=490, gain=1)

# Create single-ended input on channel 0
currentClamp = AnalogIn(ads, ADS.P0, ADS.P1)
vibrationSensor = AnalogIn(ads, ADS.P2)

with open("/mnt/data/testing/voltage_opamp_490_1_no_cap.csv", "a") as log:
    while True:
        log.write("{0}\n".format(currentClamp.value))
        # log.write("{0},{1},{2},{3}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp), currentClamp.value, vibrationSensor.value))
        # log.write("{0}\n", currentClamp.value)
