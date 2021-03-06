# Generated by Django 2.2.8 on 2020-03-02 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('area', models.CharField(max_length=30)),
                ('rent_expected', models.IntegerField()),
                ('advance_expected', models.IntegerField()),
                ('image_url', models.ImageField(upload_to='')),
                ('rental_status', models.CharField(choices=[('avail', 'Available'), ('navail', 'Not Available')], max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
