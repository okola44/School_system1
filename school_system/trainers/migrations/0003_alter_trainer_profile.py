# Generated by Django 3.2.5 on 2021-08-20 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_remove_trainer_date_of_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
