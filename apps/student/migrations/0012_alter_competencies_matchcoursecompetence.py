# Generated by Django 4.1.1 on 2022-12-10 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmatchcoursecompetence',
            name='competencies',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.competencies'),
        ),
        migrations.RemoveField(
            model_name='matchcoursecompetence',
            name='competencies',
        ),
        migrations.AddField(
            model_name='matchcoursecompetence',
            name='competencies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.competencies'),
        ),
    ]
