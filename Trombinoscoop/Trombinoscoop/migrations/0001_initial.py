# Generated by Django 5.0 on 2024-01-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_de_naissance', models.DateField()),
                ('courriel', models.EmailField(max_length=254)),
                ('tel_fixe', models.CharField(max_length=20)),
                ('tel_mobile', models.CharField(max_length=20)),
                ('mot_de_passe', models.CharField(max_length=32)),
                ('test', models.CharField(max_length=20)),
            ],
        ),
    ]