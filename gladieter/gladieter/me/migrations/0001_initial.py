# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-02 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('gtins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductInformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]