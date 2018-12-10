# Generated by Django 2.1.2 on 2018-12-10 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('hadm_id', models.CharField(blank=True, max_length=100, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('drug', models.CharField(blank=True, max_length=250, null=True)),
                ('drug_name', models.CharField(blank=True, max_length=250, null=True)),
                ('webmd_link', models.TextField(blank=True, null=True)),
                ('dose_val', models.FloatField(blank=True, null=True)),
                ('prod_strength', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]