# Generated by Django 4.1.6 on 2023-05-15 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_venuephoto_venue'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='venuephoto',
            unique_together=set(),
        ),
    ]
