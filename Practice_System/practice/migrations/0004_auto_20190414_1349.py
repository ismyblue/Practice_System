# Generated by Django 2.1.7 on 2019-04-14 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20190414_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='stu_id',
            field=models.ForeignKey(db_column='stu_id', on_delete=django.db.models.deletion.CASCADE, to='practice.Student'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='ent_id',
            field=models.IntegerField(db_column='ent_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='ent_id',
            field=models.ForeignKey(db_column='ent_id', on_delete=django.db.models.deletion.CASCADE, to='practice.Enterprise'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.IntegerField(db_column='job_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_id',
            field=models.IntegerField(db_column='menu_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='role_id',
            field=models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='practice.Role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.IntegerField(db_column='role_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_id',
            field=models.IntegerField(db_column='stu_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='tea_id',
            field=models.ForeignKey(db_column='tea_id', on_delete=django.db.models.deletion.CASCADE, to='practice.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tea_id',
            field=models.IntegerField(db_column='tea_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weekrecord',
            name='stu_id',
            field=models.ForeignKey(db_column='stu_id', on_delete=django.db.models.deletion.CASCADE, to='practice.Student'),
        ),
    ]
