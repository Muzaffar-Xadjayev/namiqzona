# Generated by Django 4.0.3 on 2022-06-18 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_tashkilotlar_t_inn_alter_tashkilotlar_t_shxr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tashkilotlar',
            name='user_id',
        ),
    ]
