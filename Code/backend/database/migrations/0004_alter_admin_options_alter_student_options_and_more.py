# Generated by Django 4.2.4 on 2023-08-19 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_admin_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.AlterModelManagers(
            name='admin',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
            ],
        ),
    ]
