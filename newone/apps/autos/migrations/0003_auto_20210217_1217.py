# Generated by Django 3.1.3 on 2021-02-17 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_auto_20210217_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autos.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='car',
            name='importation_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autos.importation', verbose_name='Importacion'),
        ),
    ]