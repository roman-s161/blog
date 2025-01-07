# Generated by Django 5.1.3 on 2024-12-25 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, default='Без описания', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='python_blog.category'),
        ),
    ]
