# Generated by Django 3.2.9 on 2022-02-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_alter_protectdataset_assessed_maturity_level_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protectdataset',
            old_name='protect_id',
            new_name='identify_id',
        ),
    ]
