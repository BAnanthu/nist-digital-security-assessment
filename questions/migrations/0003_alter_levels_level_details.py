# Generated by Django 3.2.9 on 2022-02-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_options_level_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levels',
            name='level_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
