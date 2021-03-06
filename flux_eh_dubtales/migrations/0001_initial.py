# Generated by Django 2.2.6 on 2020-01-15 11:32

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DubtalesSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_id', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('exchange_datetime', models.DateTimeField(blank=True, editable=False, null=True)),
                ('handler', models.CharField(blank=True, editable=False, max_length=300, null=True)),
                ('post_create_output', models.TextField(blank=True, null=True)),
                ('message', django_mysql.models.JSONField(default=dict)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Dubtales Submission',
                'verbose_name_plural': 'Dubtales Submissions',
            },
        ),
    ]
