# Generated by Django 4.0.1 on 2022-11-14 17:44

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('coach', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('recurrences', recurrence.fields.RecurrenceField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('categories', models.ManyToManyField(related_name='classes', to='classes.Category')),
            ],
        ),
    ]