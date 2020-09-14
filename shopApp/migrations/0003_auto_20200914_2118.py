# Generated by Django 3.0.8 on 2020-09-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_auto_20200914_2041'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email_address'),
        ),
    ]