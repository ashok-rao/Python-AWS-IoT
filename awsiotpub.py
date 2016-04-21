#!/usr/bin/python

# this source is part of my Hackster.io project:  https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will publish test mqtt messages using the AWS IoT hub
# to test this program you have to run first its companion awsiotsub.py
# that will subscribe and show all the messages sent by this program

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import os
import socket
import ssl
from time import sleep
from random import uniform

connflag = False
GPIO.setmode(GPIO.BOARD)

def on_connect(client, userdata, rc):
    print("Inside")
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+"e14.temperature"+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

#awshost = "A1K1D4ABLJYWA4.iot.eu-west-1.amazonaws.com"
awsport = 8883
clientId = "PushButton"
thingName = "PushButton"
caPath = "aws-iot-rootCA.crt"
certPath = "cert.pem"
keyPath = "privkey.pem"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

#mqttc.connect(awshost, awsport, keepalive=60)

mqttc.connect("A1K1D4ABLJYWA4.iot.eu-west-1.amazonaws.com", 8883, 60)
#mqttc.connect("iot.eclipse.org", 1883, 60)
mqttc.loop_start()

while 1==1:
    sleep(0.5)
    if GPIO.input(11):
        print("GPIO.input = %d" % GPIO.input(11))
        GPIO.output(12, False)
    else:
        GPIO.output(12, True)
        print("GPIO.input = %d" % GPIO.input(11))
        
    if connflag == True:
        #tempreading = uniform(20.0,25.0)
        ButtonState = (GPIO.input(11))
        #mqttc.publish("e14.temperature", tempreading, qos=1)
        mqttc.publish("e14.ButtonState", ButtonState, qos=1)
        #print("msg sent: e14.temperature " + "%.2f" % tempreading )
        print("msg sent: e14.ButtonState " + "%d" % ButtonState )
    else:
        print("waiting for connection...")
