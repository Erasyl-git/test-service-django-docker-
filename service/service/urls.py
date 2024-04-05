from rest_framework import routers
from django.contrib import admin
from django.urls import path
from services.views import SubscriptionView


urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()

router.register(r'api/subsriptions', SubscriptionView)

urlpatterns += router.urls


