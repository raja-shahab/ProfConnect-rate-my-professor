# Generated by Django 5.0.6 on 2024-08-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
