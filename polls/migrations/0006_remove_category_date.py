# Generated by Django 4.2.2 on 2023-07-29 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_candidate_num_of_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='date',
        ),
    ]
