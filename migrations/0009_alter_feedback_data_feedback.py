# Generated by Django 5.1.2 on 2024-11-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_arquivo_usuario_alter_usuario_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='data_feedback',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data do Feedback'),
        ),
    ]
