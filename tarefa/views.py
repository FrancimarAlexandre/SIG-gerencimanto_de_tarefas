from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import CreateFormTarefa
from .models import Tarefa
# Create your views here.
@login_required
def homepage(request):
    tarefa = Tarefa.objects.filter(usuario = request.user)
    return render(request,'homepage.html',{"contexto":tarefa})

@login_required
def create_tarfa(request):
    if request.method == 'POST':
        form = CreateFormTarefa(request.POST,user = request.user)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateFormTarefa(user=request.user)
    return render(request,'crud_tarefa/create.html',{"form":form})