# Generated by Django 4.1.1 on 2022-11-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0005_historicalpermission_isfather_permission_isfather_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalrole',
            name='description',
        ),
        migrations.RemoveField(
            model_name='role',
            name='description',
        ),
        migrations.AlterField(
            model_name='historicalpermission',
            name='isFather',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='historicalpermission',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='permission',
            name='isFather',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
