# Generated by Django 5.1.1 on 2024-09-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_arquivo_alter_conversao_nome_arquivo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivo',
            options={'verbose_name': 'Conversão', 'verbose_name_plural': 'Conversões'},
        ),
    ]
