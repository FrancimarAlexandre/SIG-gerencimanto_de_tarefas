from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required 


def registry_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Checando se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe')
            return redirect('registro') # se existir redireciona novamente para a página de registro
        # checando se o email já existe
        elif User.objects.filter(email=email).exists():
             messages.error(request, 'E-mail já cadastrado')
             return redirect('registro')
        else:
            # criando uma nova instancia de User e salvando
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Efetue login automaticamente do usuário após o registro (opcional)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    return render(request,'registration/register.html')

@login_required
def index(request):
    return render(request,'index.html')

