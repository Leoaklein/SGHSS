from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

User = get_user_model()
def login_paciente(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.tipo == "paciente":  # só pacientes podem logar aqui
            login(request, user)
            return redirect("paciente:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "paciente/login.html")

def dashboard_paciente(request):
    # Aqui depois vamos colocar a página de opções do paciente
    return render(request, "paciente/dashboard.html")


def registrar_paciente(request):
    if request.method == "POST":
        username = request.POST.get("username")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        telefone = request.POST.get('telefone')
        password = request.POST.get("password")
        confirmarpassword = request.POST.get("confirmarpassword")

        # Verificar se a senha coincide
        if password != confirmarpassword:
            messages.error(request, "As senhas não coincidem.")
            return redirect("paciente:registrar")

        # Verificar se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return redirect("paciente:registrar")
        # Criar usuário
        User.objects.create_user(username=username, password=password, cpf=cpf,telefone=telefone, tipo="paciente", data_nascimento=data_nascimento)
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect("paciente:login")

    return render(request,"paciente/registrar.html")