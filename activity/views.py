from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import generate_email_activity


@api_view(['POST'])
def start_activity(request):

    for _ in range(5):
        generate_email_activity()

    return Response({
        "message": "Email activity generated successfully"
    })