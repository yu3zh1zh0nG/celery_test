import time
from celery import Celery
import random
from flask_mail import Mail, Message
import json
from run import create_app

celery = Celery('mycelery', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')


@celery.task
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    app = create_app()
    mail = Mail(app)
    print('zzz')
    message = Message(msg['title'],sender='13135673615@163.com',
                  recipients=msg['recipients'])
    message.body = msg['info']
    with app.app_context():
        mail.send(message)
    print('发送成功')


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    print('please start your performance!')
    print('=============================')
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        print('===')
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
