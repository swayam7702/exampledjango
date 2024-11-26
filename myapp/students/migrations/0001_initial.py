# Generated by Django 5.1.2 on 2024-11-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Sample',
                'verbose_name_plural': 'Samples',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('addres', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('joinedDate', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Stud',
                'verbose_name_plural': 'Studs',
                'db_table': '',
                'managed': True,
            },
        ),
    ]