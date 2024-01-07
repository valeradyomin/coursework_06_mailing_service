from django.db import models
from django.utils import timezone

# Create your models here.

NULLABLE = {
    'null': True,
    'blank': True,
}


class Client(models.Model):
    email = models.EmailField(max_length=100, unique=True, verbose_name='почтовый адрес')
    initials = models.CharField(max_length=50, verbose_name='инициалы')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.initials} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mail(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class MailingSrv(models.Model):
    AT_ONCE = 'единоразово'
    BY_DAY = 'раз в день'
    BY_WEEK = 'раз в неделю'
    BY_MONTH = 'раз в месяц'

    FREQUENCY = [
        (AT_ONCE, 'единоразово'),
        (BY_DAY, 'раз в день'),
        (BY_WEEK, 'раз в неделю'),
        (BY_MONTH, 'раз в месяц')
    ]

    CREATED = 'создана'
    PROCESSING = 'запущена'
    FINISHED = 'завершена'

    STATUS = [
        (CREATED, 'создана'),
        (PROCESSING, 'запущена'),
        (FINISHED, 'завершена')
    ]

    name = models.CharField(max_length=25, verbose_name='наименование рассылки', **NULLABLE)
    recipients = models.ManyToManyField(Client, verbose_name='получатели рассылки')
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='письмо', **NULLABLE)
    start = models.DateTimeField(default=timezone.now, verbose_name='время начала рассылки')
    next = models.DateTimeField(default=timezone.now, verbose_name='время следующей рассылки')
    finish = models.DateTimeField(verbose_name='время завершения рассылки')
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0], verbose_name='статус рассылки')
    frequency = models.CharField(max_length=50, choices=FREQUENCY, verbose_name='периодичность рассылки')
    is_activated = models.BooleanField(default=True, verbose_name='метка активности')

    def __str__(self):
        return f'Рассылка_{self.pk}: {self.status} (с {self.start} по {self.finish} - {self.frequency})'

    class Meta:
        verbose_name = 'параметр рассылки'
        verbose_name_plural = 'параметры рассылок'


class Log(models.Model):

    attempt_time = models.DateTimeField(auto_now=True, verbose_name='время последней попытки'),
    status = models.CharField(max_length=50, verbose_name='статус попытки', default='попытка не инициирована')
    server_response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    recipient = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='получатель рассылки')
    mailing = models.ForeignKey(MailingSrv, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return f'Отчет {self.pk}:  Статус - {self.status}( Когда - {self.attempt_time})'

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
