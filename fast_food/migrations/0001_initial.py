# Generated by Django 5.0.1 on 2024-02-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsul',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('dec', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
