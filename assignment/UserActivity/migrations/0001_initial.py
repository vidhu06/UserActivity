# Generated by Django 3.0.7 on 2020-06-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('real_name', models.TextField(max_length=255)),
                ('tz', models.TextField(max_length=255)),
            ],
        ),
    ]