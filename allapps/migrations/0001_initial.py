# Generated by Django 4.2.7 on 2023-12-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
