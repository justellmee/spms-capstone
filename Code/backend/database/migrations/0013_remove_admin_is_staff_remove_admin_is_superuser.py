# Generated by Django 4.2.4 on 2023-09-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_admin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='is_superuser',
        ),
    ]
