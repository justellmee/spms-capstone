# Generated by Django 4.2.4 on 2023-09-01 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_admin_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
    ]
