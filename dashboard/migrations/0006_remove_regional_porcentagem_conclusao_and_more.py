# Generated by Django 4.2.4 on 2023-08-16 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_equipe_options_alter_loja_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regional',
            name='porcentagem_conclusao',
        ),
        migrations.AlterField(
            model_name='regional',
            name='loja_atual',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
