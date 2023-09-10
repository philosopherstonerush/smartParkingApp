from django.urls import path

from . import views

urlpatterns = [
    path("", views.showSlots, name="SlotsList"),
    path("addSensor", views.addSensor, name="addSensor"),
]