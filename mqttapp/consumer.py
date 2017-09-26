import time
import json
import logging
import random
import paho.mqtt.client as mqtt
from mqttapp import app


logger = logging.getLogger(__name__)


# def on_connect(client, userdata, flags, rc):
#     logger.info('Connected with result code: %s, flags: %s', rc, flags)
#     client.subscribe('$SYS/#')
#
# def on_message(client, userdata, msg):
#     logger.info('[{}] {}'.format(msg.topic, msg.payload))


TOPIC = 'topics/test'


class MQTTClient:
    client = None

    def __init__(self, client_id='', clean_session=True):
        self.client = mqtt.Client(client_id=client_id,
                                  clean_session=clean_session)

    def on_connect(self, client, userdata, flags, rc):
        logger.info('Connected with result code: %s, flags: %s', rc, flags)
        self.client.subscribe(TOPIC, qos=1)

    def on_message(self, client, userdata, msg):
        logger.info('[{}] {}'.format(msg.topic, msg.payload))


class Consumer(MQTTClient):
    def __init__(self, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def run(self):
        # self.client.connect(app.config['CLOUDMQTT_URL'], 1883, 60)
        try:
            self.client.connect(app.config['CLOUDMQTT_URL'])
            self.client.loop_forever()
        except KeyboardInterrupt:
            logger.info('Disconnecting')
            # self.client.disconnect()


class Publisher(MQTTClient):
    def publish(self, num_messages=5):
        logger.info('Publishing {} messages'.format(num_messages))
        self.client.connect('localhost')
        self.client.loop_start()

        for _ in range(num_messages):
            message = 'hello, World {}'.format(random.randint(1, 100))
            logger.info('Publishing message: %s', message)
            result = self.client.publish(
                TOPIC,
                payload=message,
                qos=2
            )

            logger.info('Published message, result: %s', result)
            time.sleep(1)

        self.client.disconnect()

