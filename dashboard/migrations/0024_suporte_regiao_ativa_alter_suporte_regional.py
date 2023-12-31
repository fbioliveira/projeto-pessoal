# Generated by Django 4.2.4 on 2023-08-21 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_remove_dashboard_equipes_remove_dashboard_lojas'),
    ]

    operations = [
        migrations.AddField(
            model_name='suporte',
            name='regiao_ativa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='suporte_atual', to='dashboard.regional'),
        ),
        migrations.AlterField(
            model_name='suporte',
            name='regional',
            field=models.ManyToManyField(blank=True, related_name='suporte', to='dashboard.regional'),
        ),
    ]
