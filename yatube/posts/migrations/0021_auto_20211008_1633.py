# Generated by Django 2.2.16 on 2021-10-08 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_auto_20211008_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
