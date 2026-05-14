from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import EmailAccount
from .serializers import EmailAccountSerializer


class EmailAccountViewSet(viewsets.ModelViewSet):

    queryset = EmailAccount.objects.all()

    serializer_class = EmailAccountSerializer