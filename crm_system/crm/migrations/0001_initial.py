# Generated by Django 5.0.4 on 2024-05-02 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('promotion_channel', models.CharField(max_length=100)),
                ('advertising_budget', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='contracts/')),
                ('conclusion_date', models.DateField()),
                ('validity_period', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PotentialClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('advertising_campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.advertisingcampaign')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contract')),
                ('potential_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.potentialclient')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.service'),
        ),
        migrations.AddField(
            model_name='advertisingcampaign',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.service'),
        ),
    ]
