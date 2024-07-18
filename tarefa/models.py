from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tarefa(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    titulo = models .CharField(max_length = 55)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateField()
    status = models.BooleanField(default = False)

    def __str__(self):
        return f'Tarefa {self.titulo} do usuário {self.usuario.username}'