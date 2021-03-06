# Generated by Django 2.1.7 on 2019-04-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('choice_id', models.IntegerField(primary_key=True, serialize=False)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('ent_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ent_pwd', models.CharField(max_length=20)),
                ('ent_name', models.CharField(max_length=40)),
                ('introduction', models.CharField(max_length=150)),
                ('ent_address', models.CharField(max_length=40)),
                ('ent_phone', models.CharField(max_length=11)),
                ('ent_email', models.CharField(max_length=15)),
                ('principal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=20)),
                ('job_desc', models.CharField(max_length=100)),
                ('employ_num', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('job_time', models.IntegerField(default=0)),
                ('ent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=4)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_pwd', models.CharField(max_length=20)),
                ('stu_name', models.CharField(max_length=10)),
                ('stu_age', models.IntegerField(default=0)),
                ('phone_num', models.CharField(max_length=11)),
                ('e_mail', models.CharField(max_length=15)),
                ('major', models.CharField(max_length=20)),
                ('grade', models.IntegerField(default=0)),
                ('stu_class', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=40)),
                ('political_status', models.CharField(max_length=10)),
                ('target_post', models.CharField(max_length=20)),
                ('intention_area', models.CharField(max_length=40)),
                ('resume', models.FileField(upload_to='practice/resume/')),
                ('tripartite_agreement', models.BooleanField(default=False)),
                ('practice_agreement', models.BooleanField(default=False)),
                ('employment_agreement', models.BooleanField(default=False)),
                ('tea_mark', models.IntegerField(default=0)),
                ('ent_mark', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tea_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tea_pwd', models.CharField(max_length=20)),
                ('tea_name', models.CharField(max_length=10)),
                ('tea_phone', models.CharField(max_length=11)),
                ('tea_email', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=20)),
                ('tea_post', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WeekRecord',
            fields=[
                ('weekRecord_id', models.IntegerField(primary_key=True, serialize=False)),
                ('recordContent', models.CharField(max_length=2048)),
                ('stu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Teacher'),
        ),
        migrations.AddField(
            model_name='menu',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Role'),
        ),
        migrations.AddField(
            model_name='choice',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Job'),
        ),
        migrations.AddField(
            model_name='choice',
            name='stu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Student'),
        ),
    ]
