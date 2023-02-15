# Generated by Django 3.2.16 on 2023-01-05 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='学院名称')),
            ],
            options={
                'db_table': 'stu_Faculty',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='专业名称')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentweb.faculty', verbose_name='所属学院')),
            ],
            options={
                'db_table': 'stu_Major',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, default=None, null=True, verbose_name='出生日期')),
                ('mobile', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='电话')),
                ('email', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='邮箱')),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='地址')),
                ('image', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='照片')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentweb.major', verbose_name='专业')),
            ],
            options={
                'db_table': 'stu_Student',
                'managed': True,
            },
        ),
    ]
