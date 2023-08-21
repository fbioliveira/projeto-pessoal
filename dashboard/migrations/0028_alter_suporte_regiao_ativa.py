# Generated by Django 4.2.4 on 2023-08-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_alter_suporte_regiao_ativa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='regiao_ativa',
            field=models.CharField(choices=[('afonso', 'REGIONAL AFONSO'), ('cazuza', 'REGIONAL CAZUZA'), ('coutinho', 'REGIONAL COUTINHO'), ('edivano', 'REGIONAL EDIVANO'), ('wellington', 'REGIONAL WELLINGTON')], default='Nenhuma', max_length=100),
        ),
    ]
