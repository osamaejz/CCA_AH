# Generated by Django 3.2.3 on 2021-07-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='valid',
            field=models.IntegerField(null=True),
        ),
    ]