# Generated by Django 4.0.2 on 2022-02-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0003_freepost_freecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snsapp.freepost'),
        ),
    ]
