import time
import requests
import paho.mqtt.client as paho

broker = "node.pudenko.com"
resetvalue = 0

def telegram_bot_sendtext(bot_message):
    bot_token = '1428837212:AAGr9AnSJOc4MjJTVSynivoPCvDHxyKgj6Y'
    bot_chatID = '702482339'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()




def on_message(client, userdata, message):
    # time.sleep(1)
    # print("received message =", str(message.payload.decode("utf-8")))
    if str(message.payload.decode("utf-8")):
        global resetvalue
        resetvalue = 1

def timer():
    s = 0
    m = 0
    h = 0
    while s <= 60:
        global resetvalue
        global test
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
        elif h == 24:
            telegram_bot_sendtext("Error Ivankov connect")
            s = 0
            m = 0
            h = 0
        elif resetvalue != 0:
            s = 0
            m = 0
            h = 0
            resetvalue = 0

client = paho.Client("client-linux-001")
client.on_message = on_message
client.connect(broker)
client.loop_start()
client.subscribe("Ivankov/LocalTemperature")
timer()
