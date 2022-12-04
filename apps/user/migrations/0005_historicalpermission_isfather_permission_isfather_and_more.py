# Generated by Django 4.1.1 on 2022-11-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0004_historicalpermission_isfather_historicalrole_edit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpermission',
            name='isFather',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='isFather',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalpermission',
            name='path',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='path',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
