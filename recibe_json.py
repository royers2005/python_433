#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import urllib.request

from rpi_rf import RFDevice

rfdevice = None
sensorAlertCodes = [14217875, 5365139, 16752505]
sensor_idx  = 35
url_json      = "http://192.168.0.200:8080/json.htm?username=dXNlcm5hbWU=&password=cGFzc3$verbose       = 1 # 1 to print out information to the console, 0 for silence

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GP$parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
print("Listening for codes on GPIO " + str(args.gpio))
while True:
    code = rfdevice.rx_code
    length = rfdevice.rx_pulselength
    proto = rfdevice.rx_proto
    cmd = (url_json  + str(sensor_idx) + "&switchcmd=Toggle")
#    hf = urllib.request.urlopen(cmd)
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        #code = rfdevice.rx_code
        print (code, length, proto)
        #cmd = url_json  + str(sensor_idx) + "&switchcmd=Toggle"
        #hf = urllib.urlopen(cmd)
        #if (code) in sensorAlertCodes:
        #    print (cmd)
 #           print 'Respuesta: ' + hf.read()
        #hf.close
        if  (code)  in sensorAlertCodes:
            print (cmd)
            time.sleep(2)
#    hf.close
    time.sleep(0.1)

rfdevice.cleanup()
