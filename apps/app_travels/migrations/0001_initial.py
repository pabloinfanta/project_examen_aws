# Generated by Django 2.2.4 on 2021-10-06 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_travels', to='app_users.User')),
                ('users', models.ManyToManyField(related_name='travels', to='app_users.User')),
            ],
        ),
    ]
