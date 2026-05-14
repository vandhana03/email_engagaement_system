# from django.db import models

# Create your models here.
from django.db import models
from accounts.models import EmailAccount


class Conversation(models.Model):

    sender = models.ForeignKey(
        EmailAccount,
        related_name='conversation_sender',
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        EmailAccount,
        related_name='conversation_receiver',
        on_delete=models.CASCADE
    )

    topic = models.CharField(max_length=255)

    started_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.topic