from django.urls import path
from .views import start_activity

urlpatterns = [
    path('start/', start_activity),
]