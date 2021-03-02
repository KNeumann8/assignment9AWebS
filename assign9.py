import requests
import json
from gpiozero import Button
from time import sleep
import datetime
import random

filename = "/home/pi/Desktop/Modas/log.log"

def log():
    # get current date / time
    t = datetime.datetime.now()
    # format date in json format for RESTful API
    time_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
    print(time_json)
    randomDude = random.randint(1, 3)
    # create a new event
    url = 'https://modas-jsg.azurewebsites.net/api/event/'
    headers = { 'Content-Type': 'application/json'}
    payload = { 'timestamp': time_json, 'flagged': False, 'locationId': randomDude }
    print(payload)
    # post the event
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(r.status_code)
    print(r.json())
    f = open(filename, "a")
    f.write(str(time_json) + ",False,"+ str(randomDude) +"," + str(r.status_code) +"\n")
    f.close()
    
# init button
button = Button(5)
button.when_released = log

try:
    # program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
    print("goodbye")