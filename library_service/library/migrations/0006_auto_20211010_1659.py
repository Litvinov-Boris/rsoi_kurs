# Generated by Django 3.1.2 on 2021-10-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_takenbook_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='librarybook',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='takenbook',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
