# Generated by Django 4.0.1 on 2022-11-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='currency',
            field=models.CharField(choices=[('CAD', 'cad'), ('USD', 'usd')], default='CAD', max_length=3),
        ),
    ]
