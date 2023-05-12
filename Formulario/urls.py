"""
URL configuration for Formulario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Models.Empleado.views import FormularioView
from view.HomeView import HomeView

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', FormularioView.listar_empleados, name='home'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('registrarEmpleado/', FormularioView.index, name='registrarEmpleado'),
    path('guardarEmpleado/', FormularioView.procesar_formulario, name='guardarEmpleado'),
    path('listarEmpleados/', FormularioView.listar_empleados, name='listarEmpleados'),
    path('pdfEmpleados/', FormularioView.pdf_empleados, name='pdfEmpleados'),
    path('listarCorreos/', FormularioView.listar_correos, name='listarCorreos'),
    path('editarEmpleado/<int:id_empleado>', FormularioView.editar_empleado, name='editarEmpleado'),
    path('actualizarEmpleado/<int:id_empleado>', FormularioView.actualizar_empleado, name='actualizarEmpleado'),
    path('eliminarEmpleado/<int:id_empleado>', FormularioView.eliminar_empleado, name='eliminarEmpleado'),
    path('correoEmpleado/<int:id_empleado>', FormularioView.enviar_empleado, name='correoEmpleado'),
]
