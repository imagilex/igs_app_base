# Generated by Django 5.1.2 on 2024-11-27 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igs_app_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='app',
            options={'ordering': ['posicion', 'nombre']},
        ),
    ]