# Generated by Django 4.2.5 on 2023-10-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('MovieID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('MovieTitle', models.TextField()),
                ('ReleaseDate', models.DateField()),
                ('Genre', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Rating', models.FloatField()),
                ('RunTime', models.IntegerField()),
                ('Director', models.CharField(max_length=100)),
            ],
        ),
    ]
