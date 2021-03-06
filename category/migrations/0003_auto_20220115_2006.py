# Generated by Django 3.2.9 on 2022-01-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0008_auto_20211219_1512'),
        ('category', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='function_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='function.function'),
        ),
    ]
