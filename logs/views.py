from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import EmailLog
from .serializers import EmailLogSerializer


class EmailLogViewSet(viewsets.ModelViewSet):

    queryset = EmailLog.objects.all().order_by('-created_at')

    serializer_class = EmailLogSerializer