
#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging

from rpi_rf import RFDevice

rfdevice = None

sensorAlertCodes = [14217875, 5592405, 16752505, 2]

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device$
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
print("Listening for codes on GPIO " + str(args.gpio))
while True:
    code = rfdevice.rx_code
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        #code = rfdevice.rx_code
        print (code)
        if  (code)  in sensorAlertCodes:
            print ("MATCH")
    time.sleep(0.01)
rfdevice.cleanup()
