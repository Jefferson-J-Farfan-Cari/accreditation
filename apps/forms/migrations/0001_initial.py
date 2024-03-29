# Generated by Django 4.1.1 on 2022-12-05 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_course_name_en_historicalcourse_name_en'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SyllabusAbetForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('text_book', models.CharField(blank=True, max_length=1024, null=True)),
                ('supplementary_materials', models.CharField(blank=True, max_length=1024, null=True)),
                ('subarea', models.CharField(blank=True, max_length=1024, null=True)),
                ('brief_description', models.CharField(blank=True, max_length=1024, null=True)),
                ('issues', models.CharField(blank=True, max_length=1024, null=True)),
                ('lab_practical_experiences', models.CharField(blank=True, max_length=1024, null=True)),
                ('methodology', models.CharField(blank=True, max_length=1024, null=True)),
                ('final_note_formula', models.CharField(blank=True, max_length=1024, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'verbose_name': 'Syllabus Abet Form',
                'verbose_name_plural': 'Syllabus Abet Forms',
                'db_table': 'syllabus_abet_form',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalSyllabusAbetForm',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('text_book', models.CharField(blank=True, max_length=1024, null=True)),
                ('supplementary_materials', models.CharField(blank=True, max_length=1024, null=True)),
                ('subarea', models.CharField(blank=True, max_length=1024, null=True)),
                ('brief_description', models.CharField(blank=True, max_length=1024, null=True)),
                ('issues', models.CharField(blank=True, max_length=1024, null=True)),
                ('lab_practical_experiences', models.CharField(blank=True, max_length=1024, null=True)),
                ('methodology', models.CharField(blank=True, max_length=1024, null=True)),
                ('final_note_formula', models.CharField(blank=True, max_length=1024, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course.course')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Syllabus Abet Form',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
