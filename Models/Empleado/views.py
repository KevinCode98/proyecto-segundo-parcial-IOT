from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from Models.Empleado.forms import Formulario
from Models.Empleado.models import Empleado


class FormularioView(HttpRequest):
    def index(request):
        empleado = Formulario()
        return render(request, 'EmpleadoIndex.html', {"form": empleado})

    def procesar_formulario(request):
        empleado = Formulario(request.POST)
        if empleado.is_valid():
            empleado.save()
            empleado = Formulario()
        return render(request, 'EmpleadoIndex.html', {"form": empleado, "mensaje": "OK"})

    def listar_empleados(request):
        empleados = Empleado.objects.all()
        return render(request, 'ListadoEmpleados.html', {"empleados": empleados})

    def listar_correos(request):
        empleados = Empleado.objects.all()
        return render(request, 'ListadoCorreo.html', {"empleados": empleados})

    def pdf_empleados(request):
        empleados = Empleado.objects.all()
        return render(request, 'generadorPDF.html', {"empleados": empleados})

    def editar_empleado(request, id_empleado):
        empleado = Empleado.objects.filter(id=id_empleado).first()
        form = Formulario(instance=empleado)
        return render(request, 'EmpleadoEdit.html', {"form": form, "empleado": empleado})

    def actualizar_empleado(request, id_empleado):
        empleado = Empleado.objects.get(pk=id_empleado)
        form = Formulario(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        empleados = Empleado.objects.all()
        return render(request, 'ListadoCorreo.html', {"empleados": empleados})

    def eliminar_empleado(request, id_empleado):
        empleado = Empleado.objects.get(pk=id_empleado)
        empleado.delete()
        empleados = Empleado.objects.all()
        return render(request, 'ListadoCorreo.html', {"empleados": empleados, "mensaje": "ELIMINADO"})

    def enviar_empleado(request, id_empleado):
        empleado = Empleado.objects.get(pk=id_empleado)
        nombre = empleado.nombre
        paterno = empleado.paterno
        materno = empleado.materno
        cargo = empleado.cargo
        empresa = empleado.empresa
        calle = empleado.calle
        numero_exterior = empleado.numero_exterior
        numero_interior = empleado.numero_interior
        colonia = empleado.colonia
        municipio = empleado.municipio
        estado = empleado.estado
        codigo_postal = empleado.codigo_postal
        correo = empleado.correo
        fecha_nacimiento = empleado.fecha_nacimiento
        edad = empleado.edad

        template = render_to_string('emailEmpleado.html',
                                    {
                                        'nombre': nombre,
                                        'paterno': paterno,
                                        'materno': materno,
                                        'cargo': cargo,
                                        'empresa': empresa,
                                        'calle': calle,
                                        'numero_exterior': numero_exterior,
                                        'numero_interior': numero_interior,
                                        'colonia': colonia,
                                        'municipio': municipio,
                                        'estado': estado,
                                        'codigo_postal': codigo_postal,
                                        'correo': correo,
                                        'fecha_nacimiento': fecha_nacimiento,
                                        'edad': edad,
                                    })
        subject = 'Bienvenido al equipo'

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [correo]
        )
        email.fail_silently = False
        email.send()

        empleados = Empleado.objects.all()
        return render(request, 'ListadoCorreo.html', {"empleados": empleados})
