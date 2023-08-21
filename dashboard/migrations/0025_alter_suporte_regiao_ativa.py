# Generated by Django 4.2.4 on 2023-08-21 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_suporte_regiao_ativa_alter_suporte_regional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='regiao_ativa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suporte_atual', to='dashboard.regional'),
        ),
    ]
