# Generated by Django 2.1.5 on 2019-09-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_auto_20190907_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nocheckin',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='nocheckin',
            name='cur_processer',
        ),
        migrations.RemoveField(
            model_name='nocheckinlog',
            name='nocheckin',
        ),
        migrations.RemoveField(
            model_name='nocheckinlog',
            name='processer',
        ),
        migrations.AlterField(
            model_name='attendancelog',
            name='step',
            field=models.CharField(choices=[(1, '提出申请'), (2, '部门主管处理'), (3, '校区主任处理'), (4, '审批完毕')], max_length=2, verbose_name='步骤'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='step',
            field=models.IntegerField(choices=[(1, '提出申请'), (2, '部门主管处理'), (3, '校区主任处理'), (4, '审批完毕')], verbose_name='处理步骤'),
        ),
        migrations.DeleteModel(
            name='NoCheckIn',
        ),
        migrations.DeleteModel(
            name='NoCheckInLog',
        ),
    ]
