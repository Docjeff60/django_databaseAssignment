# Generated by Django 5.1.2 on 2024-10-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_type',
            field=models.CharField(choices=[('leader', 'cohort leader'), ('deputy', 'vice leader'), ('Secretary', 'Secretary'), ('President', 'President'), ('member', 'member')], default='member', max_length=100),
        ),
    ]