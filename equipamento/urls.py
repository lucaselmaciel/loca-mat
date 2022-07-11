from django.urls import path
from . import views

urlpatterns = [
    path("/list", views.ListEquip.as_view(), name="list_equip"),
    path("/create", views.CreateEquip.as_view(), name="create_equip"),
    path("/update/<pk>", views.UpdateEquip.as_view(), name="update_equip"),
    path("/delete/<pk>", views.DeleteEquip.as_view(), name='delete_equip'),
]
