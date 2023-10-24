# Generated by Django 3.2.12 on 2023-10-01 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('start', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('fare', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sacco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('routes', models.ManyToManyField(blank=True, to='base.Routes')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, max_length=10, null=True)),
                ('seat_number', models.IntegerField(blank=True, null=True)),
                ('isBooked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=5)),
                ('registration', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('sacco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sacco')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pickuppoint', models.CharField(blank=True, max_length=100, null=True)),
                ('routes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.routes')),
                ('sacco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.sacco')),
                ('seats', models.ManyToManyField(to='base.Seat')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.vehicle')),
            ],
        ),
    ]
