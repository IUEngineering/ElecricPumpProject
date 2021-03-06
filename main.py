# ADDR Current sensor ADC 0x48, using AIN1 and AIN0 as inputs under board.
# ADDR Vibration Sensor ADC 0x49, using GND and AIN2 as inputs upper board.

import board
import busio
from datetime import datetime
import time
import os
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1115 import Mode
from namechanger import newName, addingTime
from pytz import timezone

# Mounten van de harde schrijf op de Raspberry PI
os.system("sudo mount -U 12E2C15FE2C14825 /mnt/SSDdata")

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
    with open(addingTime("/mnt/SSDdata/data.csv"), "a") as log:
        print("1")
        log.write("{0},{1}\n".format("START", datetime.now(timezone('UTC')).astimezone(timezone('Europe/Berlin'))))
        # Zippen was mislukt maar dit is hoe je het zou kunnen doen
        #zipFilesInDir("/mnt/data", "/mnt/usb1/deZipMetData.zip", lambda name: 'csv' in name)
        # time in seconds, 86400 = 24 hours
        while time.time() - start_time <= 30:
            log.write("{0},{1}\n".format(currentClamp.voltage, vibrationSensor.voltage))
            # You can enable print for testing purposes
            # print(currentClamp
            # print(vibrationSensor.voltage)

while True:
    logger()
