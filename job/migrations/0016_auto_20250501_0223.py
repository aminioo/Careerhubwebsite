# Generated by Django 3.2.5 on 2025-04-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_auto_20250501_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_industry',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_size',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_website',
        ),
        migrations.AlterField(
            model_name='job',
            name='company_description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
