import time
import paho.mqtt.client as paho

broker = "node.pudenko.com"
resetvalue = 0
s = 0
m = 0
h = 0

def restartTimer():
    resetvalue = 1
    print(resetvalue)


def on_message(client, userdata, message):
    # time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))
    if str(message.payload.decode("utf-8")):
        restartTimer()


def timer(resetvalue):
    s = 0
    m = 0
    h = 0
    while s <= 60:
        print(h, 'Hours', m, 'Minutes', s, 'Seconds', "     reset = ", resetvalue)
        time.sleep(1)
        s += 1
        if s == 60:
            m += 1
            s = 0
        elif m == 60:
            h += 1
            m = 0
            s = 0
        elif resetvalue > 0:
            s = 0
            m = 0
            h = 0
            resetvalue = 0


client = paho.Client("client-linux-001")
client.on_message = on_message
client.connect(broker)
client.loop_start()
client.subscribe("Ivankov")
timer(resetvalue)
