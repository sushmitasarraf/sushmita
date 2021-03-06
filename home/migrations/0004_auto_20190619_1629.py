# Generated by Django 2.2.2 on 2019-06-19 10:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190619_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book_author',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='price',
        ),
        migrations.AddField(
            model_name='author',
            name='author_name',
            field=models.CharField(help_text='Name of Author', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth'),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Death'),
        ),
        migrations.AddField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='author',
            name='total_book_written',
            field=models.CharField(blank=True, choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='genre of book', to='home.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(help_text='Book Author', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='generated unique id for book', primary_key=True, serialize=False, verbose_name='Book Id'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Genre', max_length=100, null=True),
        ),
    ]
