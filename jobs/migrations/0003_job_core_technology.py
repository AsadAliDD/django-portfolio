# Generated by Django 2.1.7 on 2019-04-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190331_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='core_technology',
            field=models.CharField(default='', max_length=100),
        ),
    ]
