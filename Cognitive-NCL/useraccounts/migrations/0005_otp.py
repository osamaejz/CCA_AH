# Generated by Django 3.2.3 on 2021-07-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_auto_20210712_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=20, null=True)),
                ('valid', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]