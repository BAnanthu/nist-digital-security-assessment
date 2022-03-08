# Generated by Django 3.2.9 on 2022-02-13 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='questions.levels'),
        ),
    ]
