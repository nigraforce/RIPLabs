# Generated by Django 2.1.4 on 2018-12-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBExample', '0002_auto_20181223_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
