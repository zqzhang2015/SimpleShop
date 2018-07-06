from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(recipient_email, content):
    send_mail(
        'SimpleShop Order Report',
        content,
        'report@simpleshop.com',
        [recipient_email, 'dangjoeltang@gmail.com']
    )
    return 'Email sent to {}'.format(recipient_email)