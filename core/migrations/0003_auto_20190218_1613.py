# Generated by Django 2.1.7 on 2019-02-18 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190218_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spec',
            name='projecte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
            preserve_default=False,
        ),
    ]
