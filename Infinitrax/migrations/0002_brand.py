# Generated by Django 4.2.7 on 2023-12-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infinitrax', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
