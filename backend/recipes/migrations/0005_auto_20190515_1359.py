# Generated by Django 2.2.1 on 2019-05-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190515_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preparation',
            old_name='duration',
            new_name='indice_nut',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='indice_nut',
        ),
        migrations.AddField(
            model_name='recipes',
            name='duration',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
