from django.shortcuts import render
from AppConsultorio.models import*
from AppConsultorio.forms import*
from django.template import Template,Context


def ver_consultorio(request):

    return render(request, "AppConsultorio/inicio.html")


def Ver_Doctores(request):

    if request.method == 'POST': 

        Formulario1 = form_Doctor(request.POST)

        if Formulario1.is_valid():

            info_medico = Formulario1.cleaned_data

            Medico1 = medico(nombre= info_medico['nombre'],
                             apellido = info_medico['apellido'],
                             matricula = info_medico['matricula'],)


            Medico1.save()
            message = f"El Doctor {Medico1.apellido} fue perfectamente guardado en nuestro disco de datos. "



def Ver_Clientes(request):

    if request.method == 'POST':

        Formulario2 = form_usuario(request.POST)

        if Formulario2.is_valid():

            info_usuario = Formulario2.cleaned_data

            Formulario2 = usuario(nombre= info_usuario['nombre'],
                                  apellido= info_usuario['Apellido'],
                                  documento= info_usuario['document'], )

            Formulario2.save()
            message = f"El Cliente {Formulario2.apellido} se registro correctamente con sus datos en nuestra pagina web. "







    

        









