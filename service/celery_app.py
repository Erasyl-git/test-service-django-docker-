import os
from celery import Celery
from django.conf import settings
import time


os.environ.setdefault('DJANGO_SETTINS_MODULE', 'service.settins')


app = Celery('service')
app.config_from_object('django.conf:settings')

app.conf.broker_url = settings.CELERY_BROCKER_URL
app.autodiscover_tasks()

@app.task()
def debug_task():
    time.sleep(20)
    print('hello from debig_task')
