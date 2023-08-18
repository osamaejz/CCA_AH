# Generated by Django 3.2.5 on 2021-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0012_alter_digitspantestresult_rt'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualArrayTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField()),
                ('rt', models.CharField(max_length=20, null=True)),
                ('trial_type', models.CharField(max_length=50, null=True)),
                ('trial_index', models.CharField(max_length=20, null=True)),
                ('time_elapsed', models.CharField(max_length=20, null=True)),
                ('set_size', models.CharField(max_length=20, null=True)),
                ('locations', models.CharField(max_length=500, null=True)),
                ('colours', models.CharField(max_length=500, null=True)),
                ('correct', models.CharField(max_length=20, null=True)),
                ('key_press', models.CharField(max_length=20, null=True)),
                ('target_different', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]