# Generated by Django 2.2.1 on 2019-05-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20190515_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingredient',
            field=models.TextField(default=None, max_length=5000),
        ),
    ]
