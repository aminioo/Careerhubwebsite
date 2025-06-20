# Generated by Django 3.2.5 on 2025-04-26 21:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0012_job_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='salary_max',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='webiste',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Vacancy',
        ),
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
        migrations.AddField(
            model_name='apply',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='apply',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experience_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='experience_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_level',
            field=models.CharField(choices=[('Entry Level', 'Entry Level'), ('Mid Level', 'Mid Level'), ('Senior Level', 'Senior Level'), ('Lead', 'Lead')], default='Entry Level', max_length=15),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='responsibilities',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salary_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='apply',
            name='cover_letter',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract'), ('Freelance', 'Freelance'), ('Internship', 'Internship')], max_length=15),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='job.category')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(related_name='jobs', to='job.Skill'),
        ),
        migrations.CreateModel(
            name='SavedJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'job')},
            },
        ),
    ]
