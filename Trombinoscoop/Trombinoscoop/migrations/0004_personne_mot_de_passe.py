# Generated by Django 5.0 on 2024-02-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trombinoscoop', '0003_campus_cursus_faculte_fonction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='mot_de_passe',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
