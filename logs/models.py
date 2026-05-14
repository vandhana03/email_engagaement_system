# from django.db import models

# Create your models here.
from django.db import models
from accounts.models import EmailAccount

class EmailLog(models.Model):
    sender = models.ForeignKey(
        EmailAccount,
        related_name='sent_emails',
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        EmailAccount,
        related_name='received_emails',
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=255)

    message = models.TextField()

    is_reply = models.BooleanField(default=False)

    is_positive = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    reply_text = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
