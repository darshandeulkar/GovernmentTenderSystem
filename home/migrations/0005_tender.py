# Generated by Django 4.2.1 on 2023-06-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_company_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.CharField(max_length=10)),
                ('sector_name', models.CharField(max_length=25)),
                ('Time_dur', models.CharField(max_length=25)),
                ('price', models.CharField(max_length=20)),
                ('Start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=10)),
                ('descreption', models.CharField(max_length=70)),
            ],
        ),
    ]