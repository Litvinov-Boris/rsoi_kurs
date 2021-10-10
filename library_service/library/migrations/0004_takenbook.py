# Generated by Django 3.2.7 on 2021-09-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_library_id_librarybook_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]