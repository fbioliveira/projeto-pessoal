# Generated by Django 4.2.4 on 2023-08-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_suporte_regiao_ativa_alter_suporte_regional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suporte',
            name='regiao_ativa',
        ),
    ]
