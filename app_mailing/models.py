from django.db import models

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


class MailingSrv(models.Model):

    FREQUENCY = [
        ('DAY', 'раз в день'),
        ('WEEK', 'раз в неделю'),
        ('MONTH', 'раз в месяц')
    ]

    STATUS = [
        ('CREATED', 'создана'),
        ('PROCESSING', 'запущена'),
        ('FINISHED', 'завершена')
    ]

    recipients = models.ManyToManyField(Client, verbose_name='получатели рассылки')
    start = models.DateTimeField(auto_now_add=True, verbose_name='время начала рассылки')
    finish = models.DateTimeField(verbose_name='время завершения рассылки')
    status = models.CharField(max_length=100, default=STATUS[0], verbose_name='статус рассылки')
    frequency = models.CharField(max_length=50, choices=FREQUENCY, verbose_name='периодичность рассылки')

    def __str__(self):
        return f'параметры рассылки {self.pk}: {self.status} (с {self.start} по {self.finish} - {self.frequency})'

    class Meta:
        verbose_name = 'параметр рассылки'
        verbose_name_plural = 'параметры рассылок'


class Mail(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')
    mailing_list = models.ForeignKey(
        MailingSrv, on_delete=models.CASCADE, verbose_name='рассылка', related_name='mails', **NULLABLE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Log(models.Model):

    STATUS = [
        ('success', 'успешно'),
        ('failure', 'не выполнено')
    ]

    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='время последней попытки'),
    attempt_status = models.CharField(max_length=50, choices=STATUS, verbose_name='статус попытки')
    server_response = models.CharField(verbose_name='ответ почтового сервера', **NULLABLE)
    recipient = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='получатель рассылки')
    mailings_list = models.ForeignKey(MailingSrv, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'Отчет {self.pk}: {self.attempt_status}({self.attempt_time})'

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
