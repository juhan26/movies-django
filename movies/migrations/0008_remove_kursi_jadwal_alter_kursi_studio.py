# Generated by Django 4.2.16 on 2024-11-24 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_nomor_kursi_kode_remove_kursi_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kursi',
            name='jadwal',
        ),
        migrations.AlterField(
            model_name='kursi',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.studio'),
        ),
    ]
