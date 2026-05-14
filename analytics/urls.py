from django.urls import path

from .views import (
    activity_stats,
    reputation_growth,
    daily_activity,
)

urlpatterns = [

    path('stats/', activity_stats),

    path(
        'reputation/',
        reputation_growth
    ),

    path(
        'daily-activity/',
        daily_activity
    ),
]