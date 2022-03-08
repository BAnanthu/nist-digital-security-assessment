# Generated by Django 3.2.9 on 2021-12-05 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_initial'),
        ('function', '0004_identify_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identify',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
