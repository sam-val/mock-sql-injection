# Generated by Django 3.2.4 on 2021-07-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=50)),
                ('year_released', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
