# Generated by Django 3.2.8 on 2021-10-13 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='sender',
        ),
    ]
