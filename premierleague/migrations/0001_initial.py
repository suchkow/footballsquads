# Generated by Django 4.1.5 on 2023-01-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManUtd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='false', max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank='false')),
                ('country', models.CharField(max_length=56)),
                ('market_value', models.IntegerField(blank='true')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Manchester United',
            },
        ),
    ]