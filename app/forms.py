from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    matricula = forms.CharField(label='Matrícula', max_length=10)
    data_nascimento = forms.DateField(label='Data de nascimento')
    email = forms.EmailField(label='Email')
    telefone = forms.CharField(label='Telefone', max_length=20)
    data_ingresso = forms.DateField(label='Data de ingresso')

    class Meta:
        model = Aluno
        fields = [
            'matricula',
            'data_nascimento',
            'email',
            'telefone',
            'data_ingresso'
        ]