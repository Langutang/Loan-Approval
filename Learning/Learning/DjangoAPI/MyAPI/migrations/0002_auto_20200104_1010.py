# Generated by Django 3.0.2 on 2020-01-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvals',
            name='graduated',
            field=models.CharField(choices=[('Graduated', 'Graduated'), ('Not Graduated', 'Not Graduated')], max_length=15),
        ),
    ]