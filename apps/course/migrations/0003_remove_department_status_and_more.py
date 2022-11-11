# Generated by Django 4.1.1 on 2022-10-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicaldepartment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicalperiodacademic',
            name='status',
        ),
        migrations.RemoveField(
            model_name='periodacademic',
            name='status',
        ),
        migrations.AlterField(
            model_name='component',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcomponent',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historicalstudyplan',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studyplan',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
