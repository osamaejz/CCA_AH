# Generated by Django 3.2.5 on 2021-11-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0007_auto_20211130_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='test1',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='test3',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]