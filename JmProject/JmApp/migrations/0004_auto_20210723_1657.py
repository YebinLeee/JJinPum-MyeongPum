# Generated by Django 3.2.4 on 2021-07-23 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JmApp', '0003_item_clickcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='itemForeign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JmApp.item'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.CharField(default='', max_length=50),
        ),
    ]
