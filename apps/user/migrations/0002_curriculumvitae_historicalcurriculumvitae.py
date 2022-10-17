# Generated by Django 4.1.1 on 2022-10-13 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('id_user', models.CharField(max_length=255)),
                ('professional_title', models.CharField(max_length=255)),
                ('academic_degree', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('dina_register', models.CharField(max_length=255)),
                ('experience_professional', models.CharField(max_length=255)),
                ('experience_academic', models.CharField(max_length=255)),
                ('collegue', models.CharField(max_length=255)),
                ('societies', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
                ('awards', models.CharField(max_length=255)),
                ('conferences', models.CharField(max_length=255)),
                ('programs', models.CharField(max_length=255)),
                ('other', models.CharField(max_length=255)),
                ('idioms', models.CharField(max_length=255)),
                ('courses_dictates', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Curriculum_Vitae',
                'verbose_name_plural': 'Curriculums_Vitae',
                'db_table': 'curriculum_vitae',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalCurriculumVitae',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('id_user', models.CharField(max_length=255)),
                ('professional_title', models.CharField(max_length=255)),
                ('academic_degree', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('dina_register', models.CharField(max_length=255)),
                ('experience_professional', models.CharField(max_length=255)),
                ('experience_academic', models.CharField(max_length=255)),
                ('collegue', models.CharField(max_length=255)),
                ('societies', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
                ('awards', models.CharField(max_length=255)),
                ('conferences', models.CharField(max_length=255)),
                ('programs', models.CharField(max_length=255)),
                ('other', models.CharField(max_length=255)),
                ('idioms', models.CharField(max_length=255)),
                ('courses_dictates', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Curriculum_Vitae',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
