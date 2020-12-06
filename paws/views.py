from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm, LoginForm, AnimalForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext
from django.contrib.auth.decorators import login_required

from .models import Usuario, Animal

def Inicio(request):
    if not request.user.is_authenticated:
        return render(request, 'paws/main.html')
    else:
        return redirect('/padrinho/')

@login_required(login_url='../signin',redirect_field_name=None)
def Home(request):
    if request.user.tipo != 2:
        return redirect('../ong/')
    else:
        data = {'user' : request.user, 'ongs': Usuario.objects.filter(tipo=1)}
        return render(request, 'paws/padrinho/padrinhos-home.html', data)

@login_required(login_url='../signin',redirect_field_name=None)
def pProfile(request):
    if request.user.tipo != 2:
        return redirect('../ong/')
    else:
        data = {'user':request.user, 'animais': Animal.objects.filter(padrinho=request.user)}
        return render(request, 'paws/padrinho/padrinhos-profile.html', data)

@login_required(login_url='../signin',redirect_field_name=None)
def HomeOng(request):
    if request.user.tipo != 1:
        return redirect('../padrinho/')
    else:
        if request.method == 'POST':
            form = AnimalForm(request.POST)  
            if form.is_valid():
                animal = form.save(commit=False)
                animal.ong = request.user
                animal.save()
                return redirect('../ong/')
        else:
            form = AnimalForm()

        data = {'user': request.user, 'animais': Animal.objects.filter(ong=request.user.id), 'form': form}
        return render(request, 'paws/ong/ongs-home.html', data) 

def Sign(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
         form = LoginForm(request.POST)
         email = request.POST['email']
         password = request.POST['password']
         user = authenticate(email=email, password=password)
         
         if user is not None:

                login(request, user)

                return redirect('/padrinho/')

         else:
                form.add_error('password','Usuario não autenticado, por favor, verifique seu email e senha')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'paws/signin.html', context)
 else:
    return redirect('/padrinho/')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def Cad(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return Sign(request)
    else:
        form = UserForm()

    context = {'form': form}

    return render(request, 'paws/signup.html', context)
 else:
    return redirect('/padrinho/')

@login_required(login_url='../signin',redirect_field_name=None)
def getOng(request, ong):
    if request.user.tipo != 2:
        return redirect('../../ong/')
    else:
        data = {'animais': Animal.objects.filter(ong=ong, padrinho=None), 'ong': get_object_or_404(Usuario, pk=ong)}
    return render(request, 'paws/padrinho/padrinhos-ong-profile.html', data)

@login_required(login_url='../signin',redirect_field_name=None)
def Apadrinhar(request, paw):
    if request.user.tipo != 2:
        return redirect('../ong/')
    else:
        animal  = Animal.objects.get(pk=paw)
        animal.padrinho = request.user
        animal.save()
        return redirect('../' + str(animal.ong.id))

@login_required(login_url='../signin',redirect_field_name=None)
def pOng(request):
    if request.user.tipo != 1:
        return redirect('../padrinho/')
    else:
        data = {'animais': Animal.objects.filter(ong = request.user.id, padrinho = not None), 'user': request.user}
        return render(request, 'paws/ong/ongs-profile.html', data)


@login_required(login_url='../signin',redirect_field_name=None)
def getPadrinho(request, padrinho):
    if request.user.tipo != 1:
        return redirect('../../padrinho/')
    else:
        data = {'animais': Animal.objects.filter(padrinho=padrinho), 'padrinho': get_object_or_404(Usuario, pk=padrinho)}
    return render(request, 'paws/ong/ongs-padrinho-profile.html', data)

    

