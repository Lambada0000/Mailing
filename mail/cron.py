import smtplib
from datetime import timezone, datetime, timedelta

from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from mail.models import Attempt, Newsletter


def send_newsletter(obj):
    """Отправляет рассылки"""

    try:
        server_response = send_mail(
            f'{obj.message.subject}',
            f'{obj.message.text}',
            EMAIL_HOST_USER,
            recipient_list=[client.email for client in obj.clients.all()],
            fail_silently=False,
        )
        a = Attempt.objects.create(newsletter=obj, server_response=server_response)
        if server_response:
            a.mailing_status = True
            a.save()
    except smtplib.SMTPException as e:
        Attempt.objects.create(newsletter=obj, server_response=e)
    if obj.status == 'Создана':
        obj.status = 'Запущена'
        obj.save()


def newsletter_mail():
    """Отправляет письмо с учетом периодичности рассылки"""
    zone = timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    for obj in Newsletter.objects.filter(status__in=('Создана', 'Запущена')):
        if obj.start_date < current_datetime < obj.end_date:
            attempt = Attempt.objects.filter(newsletter=obj)
            if attempt.exists():
                last_date = attempt.order_by('date').last()
                current_timedelta = current_datetime - last_date
                if current_timedelta <= timedelta(days=1) and obj.periodicity == 'Ежедневно':
                    send_newsletter(obj)
                elif current_timedelta >= timedelta(days=7) and obj.periodicity == 'Еженедельно':
                    send_newsletter(obj)
                elif current_timedelta >= timedelta(days=30) and obj.periodicity == 'Ежемесячно':
                    send_newsletter(obj)
            else:
                send_newsletter(obj)
        elif current_datetime > obj.end_date:
            obj.status = 'Завершена'
            obj.save()
