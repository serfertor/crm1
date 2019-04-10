# Generated by Django 2.1.2 on 2018-11-09 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_agecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('children_count', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
