# Generated by Django 5.0 on 2024-02-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trombinoscoop', '0005_rename_contenu_message_conteu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='conteu',
            new_name='contenu',
        ),
    ]