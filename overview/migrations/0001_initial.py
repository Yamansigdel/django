# Generated by Django 4.2.6 on 2024-09-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview_title', models.CharField(max_length=50)),
                ('overview_des', models.TextField()),
            ],
        ),
    ]
