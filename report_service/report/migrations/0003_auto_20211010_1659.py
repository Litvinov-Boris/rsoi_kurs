# Generated by Django 3.1.2 on 2021-10-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_userstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genrestat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userstat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
