# Generated by Django 3.1.7 on 2021-04-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECEapp', '0002_auto_20210401_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='year',
            field=models.IntegerField(choices=[(4, 'Final Year'), (1, 'First Year'), (2, 'Second Year'), (3, 'Third Year')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='abstract',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='project',
            name='projecttype',
            field=models.IntegerField(choices=[(3, 'Publication'), (6, 'Patent'), (2, 'Article'), (9, 'Research Internship  Report'), (7, 'Poster'), (8, 'Pre Print'), (1, 'Thsesis'), (5, 'Chapter'), (4, 'Conference Paper')], default=1, max_length=5),
        ),
    ]
