import os
from celery import Celery
import time
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')  # Изменено с 'service' на 'services'
app.config_from_object('django.conf:settings')

app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

@app.task()
def debug_task():
    time.sleep(3)
    print('hello from debug_task')

    