# Generated by Django 3.2.7 on 2021-09-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_rename_notifications_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='email',
            field=models.EmailField(blank=True, max_length=320, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
