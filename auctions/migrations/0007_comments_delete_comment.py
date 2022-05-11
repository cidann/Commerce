# Generated by Django 4.0.4 on 2022-05-11 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.auctions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
