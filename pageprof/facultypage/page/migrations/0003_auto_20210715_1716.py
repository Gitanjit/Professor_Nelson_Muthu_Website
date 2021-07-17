# Generated by Django 3.2.5 on 2021-07-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20210715_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.CharField(help_text='Type as author1 | author2 | ... and so on ', max_length=100),
        ),
        migrations.AlterField(
            model_name='publication',
            name='info',
            field=models.TextField(help_text='For journal:journal name and pages(e.g.journal name | page 52-56), book-chapters:name of the book, conferences:name of the conference and location(for e.g. conference name | Delhi), patent:patent id(for e.g PAT/ME/P14050-1/16-17) ', max_length=5000),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(help_text='For journal:title, book-chapters:title, conferences:topic, patent:title ', max_length=100),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.CharField(blank=True, help_text='For journal:issue year(e.g 116(1186):2012), book-chapters:year of publishing, conferences:year of publishing, patent:none ', max_length=20),
        ),
    ]
