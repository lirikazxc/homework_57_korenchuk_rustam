# Generated by Django 5.0.7 on 2024-07-29 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_project_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('change_user_to_project', 'Can add or delete users to project')]},
        ),
    ]
