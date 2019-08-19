from paho.mqtt.client import Client
from watcher.mqtt_modules.callbacks import *
from watcher.watcher_modules.sms import SMS
from watcher.watcher_modules.email import Email
from watcher.watcher_modules.test import Test

topics = [('test', 0), ('sms', 0), ('email', 0)]
topic_map = {'email': Email, 'sms': SMS, 'test': Test}
user_data = {'topics': topics, 'topic_map': topic_map}

mqtt_client = Client(client_id="watcher", userdata=user_data)
# mqtt_client.username_pw_set()
mqtt_client.enable_logger()
mqtt_client.on_connect = on_connect_callback
mqtt_client.on_subscribe = on_subscribe_callback
mqtt_client.on_message = on_message_callback
mqtt_client.on_disconnect = on_disconnect_callback

mqtt_client.connect_async("localhost")
mqtt_client.loop_forever()

