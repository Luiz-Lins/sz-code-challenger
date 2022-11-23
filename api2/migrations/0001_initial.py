# Generated by Django 4.1.3 on 2022-11-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anuncio_pertence_ao_imovel', models.PositiveIntegerField()),
                ('plataforma_anuncio_publicado', models.CharField(max_length=15)),
                ('tx_da_plataforma', models.DecimalField(decimal_places=2, max_digits=4)),
                ('data_hora_de_criacao', models.DateTimeField(auto_now=True)),
                ('data_hora_de_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]