# Generated by Django 4.0.1 on 2022-02-07 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='roles',
            new_name='role',
        ),
    ]
