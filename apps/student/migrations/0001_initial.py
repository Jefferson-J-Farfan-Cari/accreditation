# Generated by Django 4.1.1 on 2022-10-30 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('type', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.CharField(max_length=380)),
                ('study_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.studyplan')),
            ],
            options={
                'verbose_name': 'Competencies',
                'verbose_name_plural': 'Competencies',
                'db_table': 'competencies',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('study_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.studyplan')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
                'db_table': 'level',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(default='name sr', max_length=160)),
                ('description', models.CharField(max_length=260)),
                ('study_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.studyplan')),
            ],
            options={
                'verbose_name': 'Student Result',
                'verbose_name_plural': 'Student Results',
                'db_table': 'student_result',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchStudentResultCompetencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('competences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.competencies')),
                ('student_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentresult')),
            ],
            options={
                'verbose_name': 'Match Student Result and Competence',
                'verbose_name_plural': 'Match Student Results and Competencies',
                'db_table': 'match_sr_c',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LevelDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('description', models.CharField(max_length=380)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.level')),
            ],
            options={
                'verbose_name': 'Level Description',
                'verbose_name_plural': 'Levels Descriptions',
                'db_table': 'level_description',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalStudentResult',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('name', models.CharField(default='name sr', max_length=160)),
                ('description', models.CharField(max_length=260)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('study_plan', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.studyplan')),
            ],
            options={
                'verbose_name': 'historical Student Result',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMatchStudentResultCompetencies',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('competences', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.competencies')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student_result', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.studentresult')),
            ],
            options={
                'verbose_name': 'historical Match Student Result and Competence',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLevelDescription',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('description', models.CharField(max_length=380)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.level')),
            ],
            options={
                'verbose_name': 'historical Level Description',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLevel',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('study_plan', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.studyplan')),
            ],
            options={
                'verbose_name': 'historical Level',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCriteria',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=380)),
                ('levelSuggest', models.CharField(blank=True, max_length=32)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student_result', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.studentresult')),
            ],
            options={
                'verbose_name': 'historical Criterion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCompetencies',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('type', models.IntegerField(default=1)),
                ('name', models.CharField(db_index=True, max_length=60)),
                ('description', models.CharField(max_length=380)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('study_plan', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.studyplan')),
            ],
            options={
                'verbose_name': 'historical Competencies',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=380)),
                ('levelSuggest', models.CharField(blank=True, max_length=32)),
                ('levelDescription', models.ManyToManyField(blank=True, to='student.leveldescription')),
                ('student_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentresult')),
            ],
            options={
                'verbose_name': 'Criterion',
                'verbose_name_plural': 'Criteria',
                'db_table': 'criteria',
                'abstract': False,
            },
        ),
    ]
