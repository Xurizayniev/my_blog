# Generated by Django 4.0.5 on 2022-06-29 16:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='blogs')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='blogs.categorymodel')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]
