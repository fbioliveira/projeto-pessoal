# Generated by Django 4.2.4 on 2023-08-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_alter_suporte_equipe_alter_suporte_regiao'),
    ]

    operations = [
        migrations.AddField(
            model_name='regional',
            name='ativa',
            field=models.BooleanField(default=False),
        ),
    ]
