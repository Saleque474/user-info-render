# Generated by Django 4.1.10 on 2023-12-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.UUIDField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('type', models.CharField(default='notification', max_length=15)),
                ('sent_by', models.CharField(max_length=63)),
                ('title', models.CharField(max_length=127)),
                ('content', models.TextField(max_length=5000)),
                ('received_at', models.DateTimeField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=63)),
                ('address', models.CharField(max_length=127)),
                ('body', models.TextField(max_length=5000)),
                ('timestamp', models.DateTimeField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('phone', models.CharField(max_length=15)),
                ('last_updated', models.DateTimeField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='CallRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.device')),
            ],
        ),
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=15)),
                ('number', models.CharField(max_length=15)),
                ('duration', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.device')),
            ],
        ),
    ]
