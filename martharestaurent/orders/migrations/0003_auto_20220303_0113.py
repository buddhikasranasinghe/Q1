# Generated by Django 2.2 on 2022-03-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
