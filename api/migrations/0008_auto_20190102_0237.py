# Generated by Django 2.1.3 on 2019-01-01 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181115_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]