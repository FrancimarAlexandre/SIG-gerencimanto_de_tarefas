# Generated by Django 5.0.7 on 2024-07-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0003_alter_tarefa_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='finished_at',
            field=models.DateField(),
        ),
    ]