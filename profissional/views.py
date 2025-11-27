from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

User = get_user_model()
def login_profissional(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.tipo == "profissional":  # só pacientes podem logar aqui
            login(request, user)
            return redirect("profissional:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "profissional/login.html")

def dashboard_profissional(request):
    # Aqui depois vamos colocar a página de opções do profissional
    return render(request, "profissional/dashboard.html")

def registrar_profissional(request):
    # criar a view do cadastro
    return render(request, "profissional/registrar.html")



