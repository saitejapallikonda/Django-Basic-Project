# Generated by Django 5.0.1 on 2024-01-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0004_alter_employeeinfo_projectid'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='reason',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
