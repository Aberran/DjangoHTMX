# Generated by Django 5.0 on 2023-12-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='karticka',
            name='name',
            field=models.CharField(default='ftak', max_length=200),
        ),
    ]