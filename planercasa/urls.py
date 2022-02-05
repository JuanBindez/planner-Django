from django.urls import path, include
from .views import hello_planer
from .views import hello_contas

urlpatterns = [
    path('', hello_planer),
    path('contas/', hello_contas),
]