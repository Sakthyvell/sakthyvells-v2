# Generated by Django 4.0.1 on 2022-03-06 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]