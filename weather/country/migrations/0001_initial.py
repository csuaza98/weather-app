# Generated by Django 4.2.5 on 2023-09-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('ISOCode', models.CharField(max_length=100, verbose_name='iso_code')),
                ('flag', models.CharField(max_length=500, null=True, verbose_name='flag')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
