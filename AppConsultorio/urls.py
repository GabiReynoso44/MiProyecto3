from django.urls import path
from AppConsultorio.views import*

urlpatterns = [

    path('inicio/', ver_consultorio,name="inicio"),
    path('medicos/', Ver_Doctores,name= "medicos"),
    path('usuarios/)', Ver_Clientes,name= "usuario")
]
    
