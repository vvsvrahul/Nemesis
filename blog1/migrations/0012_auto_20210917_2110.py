# Generated by Django 3.0.3 on 2021-09-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0011_auto_20210917_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
