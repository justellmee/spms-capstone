# Generated by Django 4.2.4 on 2023-08-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
