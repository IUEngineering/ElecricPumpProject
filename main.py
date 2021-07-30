# ADDR Current sensor ADC 0x48, using AIN1 and AIN0 as inputs under board.
#
# ADDR Vibration Sensor ADC 0x49

import board
import busio
import csv
from datetime import datetime

# Voor nu van Adafruit binnenkort even zelf aanpassen
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1115 import Mode

# open the file in the write mode
f = open('/mnt/data/testing/test', 'w')

# create the csv writer
writer = csv.writer(f)

# Create an I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADC object using the I2C bus
ads = ADS.ADS1115(i2c, data_rate=860)

ads.mode = Mode.CONTINUOUS

# Create second ADC
ads2 = ADS.ADS1115(i2c, address=0x49, data_rate=860)

# Configure second ADS
ads2.mode = Mode.CONTINUOUS

# Create single-ended input on channel 0
currentClamp = AnalogIn(ads, ADS.P0, ADS.P1)
vibrationSensor = AnalogIn(ads2, ADS.P0)



with open("/mnt/data/testing/final_tests2.csv", "a") as log:
    while True:
        #log.write("{0}\n".format(currentClamp.voltage))
        log.write("{0}\n".format(vibrationSensor.voltage))
        print(vibrationSensor.voltage)
        # You can enable print for testing purposes
        #print(currentClamp.voltage)

        log.write("{0},{1},{2}\n".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], currentClamp.voltage, vibrationSensor.voltage))
