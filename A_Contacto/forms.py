from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=50)
    apellido=forms.CharField(label='Apellido', max_length=50)
    email_usuario=forms.EmailField(label='Email', required=True)
    mensaje=forms.CharField(label='Mensaje', widget=forms.Textarea)