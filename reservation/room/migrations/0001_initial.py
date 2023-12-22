# Generated by Django 4.2.7 on 2023-12-22 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')])),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('type', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Pid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Oid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('ShippingDate', models.DateField()),
                ('Pid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='room.product')),
                ('cid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='room.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='room.clienttype'),
        ),
    ]
