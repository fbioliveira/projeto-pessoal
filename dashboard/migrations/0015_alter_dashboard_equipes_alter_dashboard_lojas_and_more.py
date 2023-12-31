# Generated by Django 4.2.4 on 2023-08-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_remove_equipe_dashboard_remove_loja_dashboard_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='equipes',
            field=models.ManyToManyField(blank=True, to='dashboard.equipe'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='lojas',
            field=models.ManyToManyField(blank=True, to='dashboard.loja'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='regionais',
            field=models.ManyToManyField(blank=True, to='dashboard.regional'),
        ),
    ]
