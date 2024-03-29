# Generated by Django 4.1.1 on 2022-12-04 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portafolio', '0002_remove_folder_etapa_remove_folder_period_academic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalForm',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=120)),
                ('path', models.CharField(db_index=True, max_length=200)),
                ('state', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('folder', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='portafolio.folder')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Form',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=120)),
                ('path', models.CharField(max_length=200, unique=True)),
                ('state', models.BooleanField(default=True)),
                ('folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portafolio.folder')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'db_table': 'form',
                'abstract': False,
            },
        ),
    ]
