# Generated by Django 5.0.1 on 2024-01-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appentrega', '0002_rename_meteriales_engranajes_bengranajes_materiales_engranajes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bcentri',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bcentri',
            name='caudal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bcentri',
            name='presion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bcentri',
            name='temp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bengranajes',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bengranajes',
            name='caudal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bengranajes',
            name='presion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bengranajes',
            name='temp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btornillo',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btornillo',
            name='caudal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btornillo',
            name='presion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btornillo',
            name='temp',
            field=models.IntegerField(),
        ),
    ]
