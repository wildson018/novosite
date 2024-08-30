from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login (request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get ('email')
        senha =  request.POST.get ('senha')
        
        user = authenticate (username = username, password = senha)
        
        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('E-mail ou senha invalidos!')

def cadastro(request):
  if request.method == "GET":
    return render(request, 'usuarios/cadastro.html')
  else:
    username = request.POST.get('email')
    email = request.POST.get('email')
    password = request.POST.get('senha')
    first_name = request.POST.get('firstname')

    user =  User.objects.filter(username=username).first()

    if user:
      return HttpResponse("Usuário já existente!")
    else:
      user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name)
      user.save()

      return HttpResponse("Usuário cadastro com sucesso!")
    
def home(request):
  if request.user.is_authenticated:
   return render(request, 'usuarios/home.html')
  else:
    return HttpResponse("Faça o login acessar! ")
  
def lancar(request):
  if request.user.is_authenticated:
   return render(request, 'usuarios/lancar.html')   
  else:
    return HttpResponse("Faça o login acessar! ")
def alterar(request):
  if request.user.is_authenticated:
    return render(request, 'usuarios/alterar.html') 
  else:
    return HttpResponse("Faça o login acessar! ")

def visualizar(request):
  if request.user.is_authenticated:
     return render(request, 'usuarios/visualizar.html')
  else:
     return HttpResponse("Faça o login acessar! ")     




