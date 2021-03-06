# Generated by Django 3.2.3 on 2021-05-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_newuser_gin'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
