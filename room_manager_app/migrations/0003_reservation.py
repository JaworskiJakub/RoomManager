# Generated by Django 4.1.7 on 2023-03-17 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_manager_app', '0002_room_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_manager_app.room')),
            ],
            options={
                'unique_together': {('date', 'room_id')},
            },
        ),
    ]