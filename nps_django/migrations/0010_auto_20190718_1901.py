# Generated by Django 2.2.3 on 2019-07-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nps_django', '0009_auto_20190717_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='zip_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
