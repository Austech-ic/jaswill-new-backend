# Generated by Django 4.0 on 2024-02-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_aboutus_contactus_icon_testimony_status_ourservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
    ]