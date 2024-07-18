from django.shortcuts import render,redirect,get_object_or_404
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
            form.save_user()
            return redirect('homepage')
    else:
        form = CreateFormTarefa(user=request.user)
    return render(request,'crud_tarefa/create.html',{"form":form})

@login_required
def confirmar_tarefa(request,id_tarefa):
    if request.method == "POST":
       tarefa = get_object_or_404(Tarefa,id = id_tarefa)
       tarefa.status = True
       tarefa.save()
    return redirect("homepage")
