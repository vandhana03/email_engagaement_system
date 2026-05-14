from django.db import models


class EmailAccount(models.Model):

    email = models.EmailField(unique=True)

    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    daily_limit = models.IntegerField(default=2)

    reputation_score = models.FloatField(default=0)

    total_sent = models.IntegerField(default=0)

    total_received = models.IntegerField(default=0)

    positive_replies = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email