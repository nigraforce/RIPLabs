# Generated by Django 2.1.4 on 2018-12-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBExample', '0003_auto_20181224_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='telephone',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]