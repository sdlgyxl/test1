# Generated by Django 2.1.5 on 2019-08-30 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_menu_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='menus',
        ),
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='roles',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
