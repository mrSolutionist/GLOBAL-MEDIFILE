# Generated by Django 3.2.3 on 2021-05-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210521_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='GIN',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
