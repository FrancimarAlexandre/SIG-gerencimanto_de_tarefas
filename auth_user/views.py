from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate 
from django.contrib.auth import login
# Registro de usuário

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Checa se o username existe no banco
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe') 
            return redirect('registro')
        elif User.objects.filter(email=email).exists():
             messages.error(request, 'E-mail já cadastrado')
             return redirect('registro')
        else:
            # cria uma nova instancia do usuário e sava
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Loga automaticamente se o usuário estiver registrado coretamente (optional)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    
    return render(request, 'registration/register.html')

