from django.urls import path
from . import views

urlpatterns = [
    path("/list", views.ListEquip.as_view(), name="list_equip"),
    path("/equip-cad", views.EquipFormView.as_view(), name="equip_form"),
    path("/update/<pk>", views.UpdateEquip.as_view(), name="update_equip"),
    path("/delete/<pk>", views.DeleteEquip.as_view(), name='delete_equip'),
]
