import random

from accounts.models import EmailAccount
from logs.models import EmailLog


SUBJECTS = [
    "Business Proposal",
    "Quick Question",
    "Collaboration Opportunity",
    "Follow Up",
    "Meeting Request",
    "Partnership Inquiry",
]

MESSAGES = [
    "Hope you are doing well.",
    "Would love to connect with you.",
    "Looking forward to hearing from you.",
    "Let's discuss further opportunities.",
    "Please let me know your thoughts.",
]

REPLY_MESSAGES = [
    "Sounds great!",
    "Interested in discussing further.",
    "Thank you for reaching out.",
    "Happy to connect.",
    "Let's schedule a discussion.",
]
reply = random.choice(REPLY_MESSAGES)
reply_text=reply


def choose_sender_receiver():

    accounts = list(
        EmailAccount.objects.filter(is_active=True)
    )

    if len(accounts) < 2:
        return None, None

    recent_logs = EmailLog.objects.order_by(
        '-created_at'
    )[:20]

    recent_pairs = set()

    for log in recent_logs:
        recent_pairs.add(
            (log.sender_id, log.receiver_id)
        )

    attempts = 0

    while attempts < 10:

        sender = random.choice(accounts)

        possible_receivers = [
            acc for acc in accounts
            if acc != sender
        ]

        receiver = random.choice(possible_receivers)

        pair = (sender.id, receiver.id)

        if pair not in recent_pairs:
            return sender, receiver

        attempts += 1

    return sender, receiver


def generate_email_activity():

    sender, receiver = choose_sender_receiver()

    if not sender or not receiver:
        return

    subject = random.choice(SUBJECTS)

    message = random.choice(MESSAGES)

    EmailLog.objects.create(
        sender=sender,
        receiver=receiver,
        subject=subject,
        message=message,
        is_reply=False,
    )

    sender.total_sent += 1
    receiver.total_received += 1

    sender.save()
    receiver.save()

    simulate_reply(sender, receiver)



def simulate_reply(original_sender, original_receiver):
    should_reply = random.choice([True, False, True])
    if not should_reply:
        return
    reply_message = random.choice(REPLY_MESSAGES)
    EmailLog.objects.create(
        sender=original_receiver,
        receiver=original_sender,
        subject="Re: Follow Up",
        message=reply_message,
        is_reply=True,
        is_positive=True,
    )

    original_receiver.positive_replies += 1
    original_receiver.reputation_score += 2

    original_receiver.save()

def get_daily_activity_count():
    return random.randint(3, 10)