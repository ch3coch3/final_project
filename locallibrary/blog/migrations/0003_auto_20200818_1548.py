# Generated by Django 3.1 on 2020-08-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='other',
            field=models.CharField(default='America', max_length=200),
        ),
    ]
