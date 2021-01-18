import time
import paho.mqtt.client as paho
broker="node.pudenko.com"
reset = 0
s = 0
m = 0
h = 0

def on_message(client, userdata, message):
    # time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    if str(message.payload.decode("utf-8")):
        reset = 1


def timer(reset):
 s = 0
 m = 0
 h = 0
 while s<=60:
    print (h, 'Hours', m, 'Minutes', s, 'Seconds')
    time.sleep(1)
    s+=1
    if s == 60:
        m+=1
        s = 0
    elif m ==60:
        h+=1
        m = 0
        s = 0
    elif reset > 0:
        s = 0
        m = 0
        h = 0
        reset = 0



client= paho.Client("client-linux-001")
client.on_message = on_message
client.connect(broker)
client.loop_start()
client.subscribe("Ivankov")
timer(reset)



