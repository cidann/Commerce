# Generated by Django 4.0.4 on 2022-05-11 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_auctions_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='price',
        ),
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='auctions.auctions'),
        ),
    ]
