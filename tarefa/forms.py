from django import forms

from .models import Tarefa

class CreateFormTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo','descricao','finished_at']
        widgets = {
            'finished_at': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            "finished_at":"Data de conclusão",
        }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pega o usuário do kwargs
        super().__init__(*args, **kwargs)

    def save_user(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.usuario = self.user
        if commit:
            instance.save()
        return instance
