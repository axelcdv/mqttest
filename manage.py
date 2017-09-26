#!/usr/bin/env python
from mqttapp import app
from flask_script import Manager, Server


manager = Manager(app)
manager.add_command('runserver', Server())


@manager.command
def consumer():
    print('Starting consumer')
    from mqttapp.consumer import Consumer
    consumer = Consumer(client_id='2', clean_session=False)
    consumer.run()

@manager.command
def publisher():
    print('Starting publisher')
    from mqttapp.consumer import Publisher
    consumer = Publisher()
    consumer.publish()

if __name__ == '__main__':
    manager.run()
