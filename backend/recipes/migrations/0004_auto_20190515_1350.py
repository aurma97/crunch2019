# Generated by Django 2.2.1 on 2019-05-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipes_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='comments',
        ),
        migrations.AlterField(
            model_name='recipes',
            name='ingredient',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]
