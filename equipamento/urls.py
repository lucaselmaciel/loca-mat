from django.urls import path
from . import views

urlpatterns = [
    path("/list", views.ListEquip.as_view(), name="list_equip")
]
