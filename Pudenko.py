from multiprocessing import Process
import random
import requests
from paho.mqtt import client as mqtt_client
import pudenkotimer


broker = 'node.pudenko.com'
port = 1883
topic = "Ivankov"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'
count = 0

def timer():
 s = 0
 m = 0
 h = 0
 while s<=60:
    print (h, 'Hours', m, 'Minutes', s, 'Seconds')
    pudenkotimer.sleep(1)
    s+=1
    if s == 60:
        m+=1
        s = 0
    elif m ==60:
        h+=1
        m = 0
        s = 0

def telegram_bot_sendtext(bot_message):
    bot_token = '1428837212:AAGr9AnSJOc4MjJTVSynivoPCvDHxyKgj6Y'
    bot_chatID = '702482339'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


 # test = telegram_bot_sendtext("Error Ivankov connect")

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        data = 1
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if data == 1:
            print ("666")



    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()




if __name__ == '__main__':
    run()
    # p1 = Process(target=pudenkotimer.f())
    # p2 = Process(target=run())
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()