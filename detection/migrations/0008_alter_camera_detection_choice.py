# Generated by Django 3.2.16 on 2023-05-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0007_auto_20230418_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='detection_choice',
            field=models.CharField(choices=[('None', 'None'), ('Weapon', 'Weapon'), ('Intruder', 'Intruder')], default='None', max_length=10),
        ),
    ]