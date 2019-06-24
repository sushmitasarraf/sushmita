# Generated by Django 2.2.2 on 2019-06-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190619_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('book_author', models.CharField(help_text='Book Author', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('price', models.IntegerField(help_text='500', null=True)),
                ('genre', models.CharField(help_text='genre', max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(help_text='11/08/1998', null=True),
        ),
    ]
