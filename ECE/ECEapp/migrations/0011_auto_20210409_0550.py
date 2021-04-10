# Generated by Django 3.1.7 on 2021-04-09 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECEapp', '0010_auto_20210409_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='year',
            field=models.IntegerField(choices=[(3, 'Third Year'), (2, 'Second Year'), (1, 'First Year'), (4, 'Final Year')]),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='projecttype',
            field=models.IntegerField(choices=[(2, 'Article'), (1, 'Thsesis'), (8, 'Pre Print'), (6, 'Patent'), (3, 'Publication'), (9, 'Research Internship  Report'), (7, 'Poster'), (5, 'Chapter'), (4, 'Conference Paper')], default=1),
        ),
    ]