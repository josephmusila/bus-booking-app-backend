# Generated by Django 3.2.12 on 2023-10-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_successful', models.BooleanField(default=False)),
                ('trans_id', models.CharField(max_length=30)),
                ('bike', models.CharField(blank=True, max_length=5, null=True)),
                ('order_id', models.CharField(max_length=200)),
                ('checkout_request_id', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30)),
                ('available_balance', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='available_balance')),
                ('actual_balance', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='actual_balance')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
