from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import EmailAccount
from logs.models import EmailLog


from django.db.models.functions import TruncDate
from django.db.models import Count

@api_view(['GET'])
def activity_stats(request):

    total_accounts = EmailAccount.objects.count()

    total_logs = EmailLog.objects.count()

    positive_replies = EmailLog.objects.filter(
        is_positive=True
    ).count()

    return Response({
        "total_accounts": total_accounts,
        "total_logs": total_logs,
        "positive_replies": positive_replies,
    })


@api_view(['GET'])
def reputation_growth(request):

    accounts = EmailAccount.objects.all()

    data = []

    for account in accounts:

        data.append({
            "email": account.email,
            "reputation_score": account.reputation_score,
            "positive_replies": account.positive_replies,
            "total_sent": account.total_sent,
        })

    return Response(data)

@api_view(['GET'])
def daily_activity(request):

    stats = (
        EmailLog.objects
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('-day')
    )

    return Response(stats)