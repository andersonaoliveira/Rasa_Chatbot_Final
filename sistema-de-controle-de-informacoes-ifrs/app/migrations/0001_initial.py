# Generated by Django 4.0.6 on 2022-08-01 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0002_alter_categorias_nome_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=254)),
                ('nome_evento', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('nome_do_professor', models.CharField(blank=True, max_length=254)),
                ('sobrenome_do_professor', models.CharField(blank=True, max_length=254)),
                ('nome_da_disciplina', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('email_do_coordenador', models.EmailField(blank=True, max_length=254)),
                ('email_do_curso', models.EmailField(blank=True, max_length=254)),
                ('modalidade_do_curso', models.CharField(blank=True, max_length=254)),
                ('modalidade_de_ingresso', models.CharField(blank=True, choices=[('ENEM', 'ENEM'), ('Prova', 'Prova'), ('Pessoa Indígena', 'Pessoa Indígena'), ('Processo Seletivo EJA', 'Processo Seletivo EJA'), ('Sorteio', 'Sorteio')], max_length=100)),
                ('nome_do_curso', models.CharField(blank=True, max_length=254)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('semestre', models.IntegerField(blank=True, null=True)),
                ('link_1', models.CharField(blank=True, max_length=254)),
                ('link_2', models.CharField(blank=True, max_length=254)),
                ('link_3', models.CharField(blank=True, max_length=254)),
                ('foto_1', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('foto_2', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('foto_3', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('arquivo_1', models.FileField(blank=True, upload_to='arquivo/%d/%m/%Y/')),
                ('arquivo_2', models.FileField(blank=True, upload_to='arquivo/%d/%m/%Y/')),
                ('arquivo_3', models.FileField(blank=True, upload_to='arquivo/%d/%m/%Y/')),
                ('forma_de_ingresso', models.CharField(blank=True, max_length=254)),
                ('requisitos', models.CharField(blank=True, max_length=254)),
                ('turno', models.CharField(blank=True, max_length=50)),
                ('numero_de_vagas', models.IntegerField(blank=True, null=True)),
                ('coordenador_do_curso', models.CharField(blank=True, max_length=254)),
                ('nome_do_requerimento', models.CharField(blank=True, max_length=254)),
                ('nome_do_sistema', models.CharField(blank=True, max_length=254)),
                ('data_de_inicio', models.CharField(blank=True, max_length=10)),
                ('data_de_fim', models.CharField(blank=True, max_length=10)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('visivel', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categorias')),
            ],
        ),
    ]