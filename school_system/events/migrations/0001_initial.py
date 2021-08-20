# Generated by Django 3.2.5 on 2021-08-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(blank=True, max_length=10, null=True)),
                ('event_id', models.CharField(blank=True, max_length=10, null=True)),
                ('event_name', models.CharField(blank=True, max_length=20, null=True)),
                ('event_duration', models.DurationField(blank=True, null=True)),
                ('event_planner', models.CharField(blank=True, max_length=20, null=True)),
                ('event_approved_by', models.CharField(blank=True, max_length=20, null=True)),
                ('event_participants', models.TextField(blank=True, null=True)),
                ('event_date_and_time', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
