# Generated by Django 5.1.1 on 2024-10-01 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id_ci', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('antiguedad_cte_anos', models.IntegerField()),
                ('antiguedad_cte_meses', models.IntegerField()),
                ('probabilidad_vida_se_mortal', models.IntegerField()),
                ('enfermedades_previas', models.CharField(max_length=2)),
                ('detalle_enfermedad', models.CharField(blank=True, max_length=100, null=True)),
                ('familiar_enfermedad', models.CharField(max_length=2)),
                ('cod_cliente', models.ForeignKey(db_column='cod_cliente', on_delete=django.db.models.deletion.CASCADE, to='gestion_clientes.cliente')),
            ],
        ),
    ]
