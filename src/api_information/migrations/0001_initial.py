# Generated by Django 3.2.8 on 2021-10-25 10:00

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('avatar', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]