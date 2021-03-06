# Generated by Django 3.2.5 on 2021-08-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=10, null=True)),
                ('last_name', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'Other')], max_length=1)),
                ('email_adress', models.EmailField(blank=True, max_length=254, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('class_name', models.CharField(max_length=10)),
                ('date_of_hire', models.DateField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('county_district', models.CharField(default='nairobi', max_length=20)),
                ('national_id', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(blank=True, choices=[('E', 'English'), ('K', 'Kinyarwanda'), ('K', 'Kiswahili')], max_length=2, null=True)),
                ('date_of_enrollment', models.DateField(blank=True, null=True)),
                ('contract', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]
