# Generated by Django 4.2.1 on 2023-05-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("paterno", models.CharField(max_length=100)),
                ("materno", models.CharField(max_length=100)),
                ("cargo", models.CharField(max_length=100)),
                ("empresa", models.CharField(max_length=100)),
                ("calle", models.CharField(max_length=100)),
                ("numero_exterior", models.IntegerField()),
                ("numero_interior", models.IntegerField()),
                ("colonia", models.CharField(max_length=50)),
                ("municipio", models.CharField(max_length=50)),
                ("estado", models.CharField(max_length=50)),
                ("codigo_postal", models.IntegerField()),
                ("correo", models.CharField(max_length=100)),
                ("fecha_nacimiento", models.DateField()),
                ("edad", models.IntegerField()),
            ],
        ),
    ]
