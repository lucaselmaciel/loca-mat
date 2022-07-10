from django.urls import path
from . import views

urlpatterns = [
    path('/list', views.ListarPessoas.as_view()),
    path('/create-pessoa', views.CriarPessoa.as_view(), name='pessoa_add'),
    path('/<pk>/update', views.EditarPessoa.as_view(), name='pessoa_edit')
]
