import board
import busio
import csv
from time import sleep, strftime, time
from gpiozero import CPUTemperature

# Create CPU object
cpu = CPUTemperature()


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
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
currentClamp = AnalogIn(ads, ADS.P0)
vibrationSensor = AnalogIn(ads, ADS.P1)

# print("{:>5}\t{:>5}\t{:>5}\t{:>5}".format("raw A0", "v A0", "raw A1", "v A1"))

# while True:
#     print("{:>5}\t{:>5.3f}\t{:>5}\t{:>5.3f}".format(currentClamp.value, currentClamp.voltage, vibrationSensor.value, vibrationSensor.voltage))
#
#
#     #time.sleep(0.2)

with open("/mnt/data/testing/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1},{2},{3}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp), currentClamp.value, vibrationSensor.value))
        sleep(1)



