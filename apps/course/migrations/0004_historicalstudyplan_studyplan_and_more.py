# Generated by Django 4.1.1 on 2022-10-15 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_remove_course_id_remove_historicalcourse_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalStudyPlan',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Study_Plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Study_Plan',
                'verbose_name_plural': 'Study_Plans',
                'db_table': 'study_plan',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='historicalcurriculum',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='curriculum',
        ),
        migrations.RemoveField(
            model_name='historicalcourse',
            name='curriculum',
        ),
        migrations.DeleteModel(
            name='Curriculum',
        ),
        migrations.DeleteModel(
            name='HistoricalCurriculum',
        ),
        migrations.AddField(
            model_name='course',
            name='study_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.studyplan'),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='study_plan',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.studyplan'),
        ),
    ]
