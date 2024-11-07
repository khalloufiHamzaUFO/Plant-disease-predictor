# Generated by Django 4.1.13 on 2024-10-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypeMaladie', '0001_initial'),
        ('Maladie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maladie',
            name='types',
            field=models.ManyToManyField(related_name='maladies', to='TypeMaladie.typemaladie', verbose_name='Types de maladies'),
        ),
    ]
