# Generated by Django 4.2 on 2024-09-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen'),
        ),
    ]
