# Generated by Django 3.2.5 on 2021-08-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anescort', '0003_alter_escort_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escort',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]