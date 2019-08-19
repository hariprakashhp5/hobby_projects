
def on_connect_callback(client, userdata, flags, rc):
	print('Connection Response: {}'.format(rc))
	client.subscribe(userdata['topics'])


def on_message_callback(client, userdata, message):
	instance = userdata['topic_map'][message.topic]
	instance(message.payload).execute()


def on_disconnect_callback(client, userdata, rc):
	if rc != 0:
		print('Connection Terminated Unexpectedly!!')
	else:
		print('Terminating Peacefully')


def on_subscribe_callback(client, userdata, mid, granted_qos):
	pass
