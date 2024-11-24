# Generated by Django 4.2.16 on 2024-11-24 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_kursi_kode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kursi',
            old_name='kode',
            new_name='nomor',
        ),
        migrations.RemoveField(
            model_name='kursi',
            name='studio',
        ),
        migrations.RemoveField(
            model_name='kursi',
            name='tersedia',
        ),
        migrations.AddField(
            model_name='kursi',
            name='jadwal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.jadwal'),
        ),
        migrations.AddField(
            model_name='kursi',
            name='status',
            field=models.CharField(default='tersedia', max_length=20),
        ),
    ]
