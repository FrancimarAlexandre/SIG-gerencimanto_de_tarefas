from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name ='homepage'),
    path('create/',views.create_tarfa,name ='create'),
    path('confirmar/<int:id_tarefa>/',views.confirmar_tarefa,name ='confirm'),
    path('delete/<int:id_tarefa>/',views.delete_tarefa,name ='delete'),
    path('update/<int:id_tarefa>/',views.update_tarefa,name ='update'),
]