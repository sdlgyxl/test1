# Generated by Django 2.1.5 on 2019-08-30 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20190830_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['id'], 'permissions': (('查看教师', '允许查看教师信息'), ('增加教师', '允许增加教师信息')), 'verbose_name': '教师', 'verbose_name_plural': '教师'},
        ),
    ]
