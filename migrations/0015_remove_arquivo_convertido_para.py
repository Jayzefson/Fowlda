# Generated by Django 5.1.2 on 2024-12-09 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_arquivo_convertido_para'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivo',
            name='convertido_para',
        ),
    ]
