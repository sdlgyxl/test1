# Generated by Django 2.1.5 on 2019-09-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0020_outwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outwork',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='outwork',
            name='auditor',
        ),
        migrations.DeleteModel(
            name='OutWork',
        ),
    ]
