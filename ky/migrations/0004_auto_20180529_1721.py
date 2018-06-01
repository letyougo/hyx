# Generated by Django 2.0.5 on 2018-05-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ky', '0003_auto_20180528_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='english_class_score',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='final_rank',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_rank',
            field=models.IntegerField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_total',
            field=models.IntegerField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_cross_major',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_fudaogongzuoqun',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_passed',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_stay',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_war_more',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_weixunqun',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_wokring',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xiaoqugroup',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xieyi_back',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_xieyi_send',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_zhinanqun',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='politic_class_score',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pro_class_score',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_rank',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_score',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
