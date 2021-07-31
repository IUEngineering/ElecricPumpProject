# ADDR Current sensor ADC 0x48, using AIN1 and AIN0 as inputs under board.
# ADDR Vibration Sensor ADC 0x49, using GND and AIN2 as inputs upper board.

import board
import busio
import csv
from datetime import datetime
import time

# Voor nu van Adafruit binnenkort even zelf aanpassen
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1115 import Mode
from zippernamechanger import newName, zipFilesInDir


# # open the file in the write mode
# f = open('/mnt/data/', 'w')
#
# # create the csv writer
# writer = csv.writer(f)

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


def logger():
    start_time = time.time()
    with open(newName("/mnt/usb1/data.csv"), "a") as log:
        print("1")
        log.write("{0},{1}\n".format("START", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]))
        zipFilesInDir("/mnt/data", "/mnt/usb1/DataZip.zip", lambda name: 'csv' in name)

        # time in seconds, 1440 = 24 hours
        while time.time() - start_time <= 60:
            log.write("{0},{1}\n".format(currentClamp.voltage, vibrationSensor.voltage))
            # You can enable print for testing purposes
            # print(currentClamp
            # print(vibrationSensor.voltage)

while True:
    logger()
