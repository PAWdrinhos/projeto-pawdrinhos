# Generated by Django 3.1.3 on 2020-12-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paws', '0002_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='desc',
            field=models.TextField(default='Nenhuma descrição adicionada'),
            preserve_default=False,
        ),
    ]