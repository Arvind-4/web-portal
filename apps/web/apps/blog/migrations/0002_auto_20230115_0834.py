# Generated by Django 3.2.16 on 2023-01-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-publish', '-updated', '-created')},
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
