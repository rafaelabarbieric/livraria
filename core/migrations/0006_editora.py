# Generated by Django 5.1.7 on 2025-04-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
            ],
        ),
    ]
