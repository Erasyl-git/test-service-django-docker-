from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client
from .task import set_price

class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()


class Plan(models.Model):
    PLAN_TYPES = {
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    }    

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=50)
    discount_percent = models.PositiveIntegerField(default=0, validators=[
                                                        MaxValueValidator(80)
                                                    ])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent



    def save(self, *args, **kwargs):
        if self.discount_percent != self.__discount_percent:   
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)
            return super().save(*args,**kwargs)
    

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)    
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)   
    price = models.PositiveIntegerField(default=0)

    
