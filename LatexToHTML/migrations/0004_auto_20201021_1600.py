# Generated by Django 3.1.2 on 2020-10-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatexToHTML', '0003_auto_20201021_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambio',
            name='html',
            field=models.TextField(blank=True, null=True),
        ),
    ]
