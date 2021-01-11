from django import forms

class EnviarMensaje(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}), max_length=200, required=True)
    desde_email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Tu e-mail'}), max_length=200, required=True)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'placeholder': 'Adelante. Te escuchamos'}), max_length=1500, required=True)
    
