# Generated by Django 2.1.4 on 2019-02-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190217_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='link_template',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]