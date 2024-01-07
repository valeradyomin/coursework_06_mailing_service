from datetime import datetime, timedelta
import pytz
from django.core.mail import send_mail
from django.conf import settings
from app_mailing.models import MailingSrv, Log


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    week = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    mailings = MailingSrv.objects.all().filter(status='создана')\
        .filter(is_activated=True)\
        .filter(next__lte=datetime.now(pytz.timezone('Europe/Moscow')))\
        .filter(finish__gte=datetime.now(pytz.timezone('Europe/Moscow')))

    for mailing in mailings:
        mailing.status = 'запущена'
        mailing.save()
        emails_list = [client.email for client in mailing.recipients.all()]

        result = send_mail(
            # subject=mailing.mail.subject,
            subject="Hi",
            # message=mailing.mail.content,
            message='WTF',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        )

        if result == 1:
            status = 'успешно отправлено'
        else:
            status = 'ошибка отправления'

        log = Log(mailing=mailing, status=status)
        log.save()

        if mailing.frequency == 'раз в день':
            mailing.next = log.attempt_time + day
        elif mailing.frequency == 'раз в неделю':
            mailing.next = log.attempt_time + week
        elif mailing.frequency == 'раз в месяц':
            mailing.next = log.attempt_time + month
        elif mailing.frequency == 'единоразово':
            mailing.next = mailing.end

        if mailing.next < mailing.end:
            mailing.status = 'создана'
        else:
            mailing.status = 'завершена'
        mailing.save()
