# Generated by Django 3.0.7 on 2020-06-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserActivity', '0003_auto_20200605_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
