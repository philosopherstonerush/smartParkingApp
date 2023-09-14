from django.urls import path

from . import views

urlpatterns = [
    path("", views.showSlots, name="SlotsList"),
    path("addSensor", views.addSensor, name="addSensor"),
    path("remove/<id>", views.removeParking, name="remove"),
    path("book/<id>", views.bookParking, name="bok")
]