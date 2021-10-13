from django.db import models

# Create your models here.


class Email(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

