# Generated by Django 3.2.9 on 2021-12-12 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20211205_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifydataset',
            name='Assessed_Maturity_Level_value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identify_Assessed_Maturity_Level_value', to='report.threatscoringtable'),
        ),
    ]
