# Generated by Django 2.1.5 on 2019-08-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='部门名称')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='部门说明')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Department', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
    ]
