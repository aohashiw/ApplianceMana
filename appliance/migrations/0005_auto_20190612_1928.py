# Generated by Django 2.2 on 2019-06-12 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appliance', '0004_datacord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacord',
            name='pid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='data', to='appliance.Appliance', verbose_name='损坏仪器'),
        ),
    ]
