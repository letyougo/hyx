# Generated by Django 2.0.5 on 2018-09-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ky', '0006_auto_20180607_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='adviser',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='apply_time',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='author',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='background',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='due_year',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='在职或再读'),
        ),
        migrations.AlterField(
            model_name='student',
            name='extend',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='old_major',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='old_school',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='remark',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='source',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bachelor_major',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bachelor_school',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bank_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bank_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birth',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='english_class_score',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='final_rank',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_rank',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_total',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fudao_school',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='idcard',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_cross_major',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_fudaogongzuoqun',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_passed',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_stay',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_war_more',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_weixunqun',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_wokring',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xiaoqugroup',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xieyi_back',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xieyi_send',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_zhinanqun',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='job',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='join_year',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='passed_type',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='politic_class_score',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pro_class_score',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='remark',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school_312',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_rank',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_score',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='study_type',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='study_year',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='train_records',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
