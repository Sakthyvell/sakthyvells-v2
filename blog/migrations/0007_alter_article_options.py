# Generated by Django 4.0.1 on 2022-03-30 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_visibility'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-updated_on'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
