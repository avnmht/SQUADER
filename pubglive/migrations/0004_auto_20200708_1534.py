# Generated by Django 2.2 on 2020-07-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubglive', '0003_auto_20200708_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainform',
            name='ingamename',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
