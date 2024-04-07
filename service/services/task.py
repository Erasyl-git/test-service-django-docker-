from celery import shared_task
from django.db.models import F
import time
from celery_singleton import Singleton


@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription


    time.sleep(4)


    subscription = Subscription.objects.filter(id=subscription_id).annotate(annotate_price=F('service__full_price') - 
                    F('service__full_price') * F('plan__discount_percent') / 100.00).first()

    subscription.price = subscription.annotate_price
    subscription.save()
