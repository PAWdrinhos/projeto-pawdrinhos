# -*- coding: utf-8 -*-
from django import forms
from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField, BRStateChoiceField
from localflavor.br.validators import BRCNPJValidator, BRCPFValidator
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from .tools import validar_cnpj, validar_cpf

from .models import Usuario, Animal

class UserForm(forms.ModelForm):

    name    = forms.CharField(required=True,widget = forms.TextInput())
    documento = forms.CharField(required=True,widget = forms.TextInput(attrs={'placeholder': 'CPF ou CNPJ'}))
    state   = BRStateChoiceField(required=True)
    city    = forms.CharField(required=True,widget= forms.TextInput())
    cep     = BRZipCodeField(required=True, widget = forms.TextInput(attrs={'placeholder': 'EX: 00000-000'}))
    email   = forms.EmailField(required=True,widget=forms.TextInput())
    password   = forms.CharField(required=True,widget=forms.PasswordInput())
    pword2  = forms.CharField(required=True,widget=forms.PasswordInput())
    tipo    = forms.ChoiceField(required=True,choices=Usuario.Suit.choices,widget=forms.RadioSelect())


    class Meta:
        model = Usuario
        fields = ['name', 'documento', 'state', 'city', 'cep', 'email', 'password', 'tipo', 'pword2']
    
    def clean_password(self):

        data = super().clean()

        if len(data.get('password')) < 8:
            raise forms.ValidationError('A senha precisa conter no mínimo 8 caracteres')

        return data.get('password')

    def clean_pword2(self):
        data = super().clean()
            
        pw = data.get('password')
        pw2 = data.get('pword2')

        if pw != pw2:
            raise forms.ValidationError('As senhas são conferem. Tente novamente!')

        return data.get('pword2')
    
    def clean_documento(self):
        
        data = super().clean()
        cp = data.get('documento')

        if not validar_cpf(cp) and not validar_cnpj(cp):
            raise forms.ValidationError('Informe um documento válido.')

        return data.get('documento')

    def save(self, commit=True):
      s = super().save(commit=False)
      s.password = make_password(s.password, salt=None, hasher='default')
      s.username = s.email
      return s.save()


class LoginForm(forms.ModelForm):

    email = forms.EmailField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['email', 'password']


class AnimalForm(forms.ModelForm):
    nome = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Nome do bichinho'}))
    classe    =forms.ChoiceField(choices=Animal.Suit.choices, widget=forms.Select())
    desc = forms.CharField(required = True, widget=forms.Textarea(attrs={'placeholder': 'Conte como ele é...', 'name':'descricao'}))

    class Meta:
        model = Animal
        fields = ['nome', 'classe', 'desc']














        

