from celery import shared_task

from .services import (
    generate_email_activity,
     get_daily_activity_count
)


@shared_task
def run_email_activity():
    count = get_daily_activity_count()
    for _ in range(count):
        generate_email_activity()

    return "Activity Completed"