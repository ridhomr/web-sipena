# Generated by Django 3.1.12 on 2021-09-16 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jurusan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telpon', models.CharField(max_length=100, null=True)),
                ('rt', models.CharField(max_length=100)),
                ('rw', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
                ('tanggal_lahir', models.DateField(null=True)),
                ('status', models.CharField(max_length=50)),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggota.jurusan')),
            ],
        ),
    ]