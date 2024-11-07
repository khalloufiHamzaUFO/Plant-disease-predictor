# Generated by Django 5.1.2 on 2024-10-26 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemandeTraitement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('commentaire', models.TextField(blank=True)),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendez_vous', to='DemandeTraitement.demandetraitement')),
            ],
        ),
    ]
