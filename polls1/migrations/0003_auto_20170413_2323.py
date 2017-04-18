# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
                ('user_mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=1000),
        ),
    ]
