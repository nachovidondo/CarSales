# Generated by Django 3.1.3 on 2021-02-17 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('description', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Importation',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Importacion',
                'verbose_name_plural': 'Importaciones',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('brand', models.CharField(max_length=150, verbose_name='Marca')),
                ('model', models.IntegerField(verbose_name='Modelo')),
                ('colour', models.CharField(max_length=100, verbose_name='Color')),
                ('category_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.category', verbose_name='Categoria')),
                ('importation_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.importation', verbose_name='Importacion')),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
            },
            bases=('base.basemodel',),
        ),
    ]
