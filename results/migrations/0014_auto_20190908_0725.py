# Generated by Django 2.2.5 on 2019-09-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_auto_20190907_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='club_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='event_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='rowing_CRI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='rowing_CRI_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='sculling_CRI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='sculling_CRI_max',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]