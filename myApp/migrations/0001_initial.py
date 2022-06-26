# Generated by Django 4.0.5 on 2022-06-18 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IqtisodiyZonalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Viloyatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tashkilotlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_established', models.DateTimeField()),
                ('director', models.CharField(max_length=150)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('t_address', models.CharField(max_length=300)),
                ('t_inn', models.IntegerField(default=0, max_length=100)),
                ('t_shxr', models.IntegerField(max_length=150)),
                ('t_area', models.FloatField(default=0)),
                ('t_investitsiya', models.FloatField(default=0)),
                ('t_xodimlar', models.IntegerField(default=0)),
                ('export', models.FloatField(default=0)),
                ('import_price', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('i_zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.iqtisodiyzonalar')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.viloyatlar')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='iqtisodiyzonalar',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.viloyatlar'),
        ),
    ]
