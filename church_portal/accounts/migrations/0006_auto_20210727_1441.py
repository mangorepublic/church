# Generated by Django 3.1.7 on 2021-07-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210726_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='church_branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customusers',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]