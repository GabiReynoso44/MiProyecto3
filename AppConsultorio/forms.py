from django import forms


class form_Doctor(forms.Form):

   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    matricula = forms.IntegerField()

class form_usuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    documento = forms.IntegerField()    


class form_individuo(forms.Form):

    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=15)
    Fecha_nacimiento = forms.DateField()

   
class form_busqueda_doctor(forms.Form):
    apellido_doctor = forms.CharField(max_length=30,label="APELLIDO DOCTOR")

class form_busqueda_usuario(forms.Form):
    apellido_usuario = forms.CharField(max_length=30,label="APELLIDO USUARIO")    


class form_busqueda_individuo(forms.Form):
    apellido_individuo = forms.CharField(max_length=30,label="APELLIDO Individuo")
