from django.urls import path,include
from Auth_user import views as Aviews
from Tarefas import views as Tviews
urlpatterns = [
    path('',Tviews.index,name ='homepage'),
    path('accounts/registry/',Aviews.registry_user,name="registro"),
    path('accounts/',include('django.contrib.auth.urls')),
]