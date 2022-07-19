from django.urls import path
from . import views

urlpatterns = [
    path("/list", views.ListEquip.as_view(), name="list_equip"),
    path("/equip-cad", views.EquipFormView.as_view(), name="equip_form"),
    path("/update/<pk>", views.UpdateEquip.as_view(), name="update_equip"),
    path("/delete/<pk>", views.DeleteEquip.as_view(), name='delete_equip'),
    path("/list-modelos", views.ListModelo.as_view(), name='list_modelo'),
    path("/create-modelo", views.CreateModeloFormView.as_view(), name='create_modelo'),
    path("/update-modelo/<pk>", views.UpdateModeloFormView.as_view(), name='update_modelo'),
    path("/delete-modelo/<pk>", views.DeleteModelo.as_view(), name="delete_modelo"),
    path("/list-locacoes", views.ListLocacoesView.as_view(), name='list_locacoes'),
    path("/create-locacao", views.CreateLocacaoFormView.as_view(), name='create_locacao'),
]
