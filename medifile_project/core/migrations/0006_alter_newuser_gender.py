# Generated by Django 3.2.3 on 2021-05-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_newuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='gender',
            field=models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')], default=True, null=True),
        ),
    ]
