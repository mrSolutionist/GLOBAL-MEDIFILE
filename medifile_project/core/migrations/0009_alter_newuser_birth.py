# Generated by Django 3.2.3 on 2021-05-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_newuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='birth',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
