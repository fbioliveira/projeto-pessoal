# Generated by Django 4.2.4 on 2023-08-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_remove_suporte_regional_suporte_regiao_ativa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suporte',
            old_name='regiao_ativa',
            new_name='regiao',
        ),
    ]
