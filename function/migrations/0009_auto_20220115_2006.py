# Generated by Django 3.2.9 on 2022-01-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20220115_2006'),
        ('function', '0008_auto_20211219_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifymaturityroadmap',
            name='assessed_maturity_level_value',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='identify',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s', to='category.category'),
        ),
    ]
