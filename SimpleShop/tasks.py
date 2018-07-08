from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(recipient_email, content, subject='SimpleShop Order Report',
               contact_email='report@simpleshop.com'):
    send_mail(
        subject,
        content,
        contact_email,
        [recipient_email, 'dangjoeltang@gmail.com']
    )
    return 'Email sent to {}'.format(recipient_email)

