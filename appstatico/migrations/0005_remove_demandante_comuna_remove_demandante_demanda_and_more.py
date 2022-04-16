# Generated by Django 4.0.4 on 2022-04-16 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstatico', '0004_alter_demanda_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandante',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='demandante',
            name='demanda',
        ),
        migrations.AddField(
            model_name='demanda',
            name='apellido_demandado',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='apellido_demandante',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='comuna_demandado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comuna_demandado', to='appstatico.comuna'),
        ),
        migrations.AddField(
            model_name='demanda',
            name='comuna_demandante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comuna_demandante', to='appstatico.comuna'),
        ),
        migrations.AddField(
            model_name='demanda',
            name='dv_demandado',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='dv_demandante',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='nombre_demandado',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='nombre_demandante',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='rut_demandado',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='rut_demandante',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='telefono_demandado',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='telefono_demandante',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Demandado',
        ),
        migrations.DeleteModel(
            name='Demandante',
        ),
    ]