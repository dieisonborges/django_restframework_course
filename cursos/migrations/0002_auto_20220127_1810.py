# Generated by Django 3.2.11 on 2022-01-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='cursos.course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Avaliação'),
        ),
    ]