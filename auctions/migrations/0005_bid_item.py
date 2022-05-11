# Generated by Django 4.0.4 on 2022-05-11 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctions_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions'),
            preserve_default=False,
        ),
    ]