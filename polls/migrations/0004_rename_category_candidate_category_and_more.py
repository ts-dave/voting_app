# Generated by Django 4.2.2 on 2023-06-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_candidate_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='num_of_votes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
