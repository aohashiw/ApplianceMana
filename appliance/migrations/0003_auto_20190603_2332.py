# Generated by Django 2.2 on 2019-06-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliance', '0002_auto_20190428_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repaircord',
            name='finish_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='维修成功时间'),
        ),
    ]
