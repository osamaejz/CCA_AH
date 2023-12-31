# Generated by Django 3.2.3 on 2021-06-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='birthyear',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='useraccounts.users')),
            ],
        ),
    ]
