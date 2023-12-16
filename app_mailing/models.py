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
