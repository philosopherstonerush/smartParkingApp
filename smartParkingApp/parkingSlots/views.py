from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Slot
from django.views.decorators.csrf import csrf_protect
import json
from djongo import models
import bson

def showSlots(request):
    if request.method == "GET":
        items = Slot.objects.all()
        return render(request, "list.html", context= {
            "items": items
        })

@csrf_protect
def addSensor(request):
    if request.method == "POST":
        content = Slot()
        content.sensorNo = int(request.POST["sensorNo"])
        content.plotNo = int(request.POST["plotNo"])
        content.status = request.POST["status"]
        content.save()
        return redirect("/")
    if request.method == "GET":
        return render(request, "newPlot.html")
    
@csrf_protect
def removeParking(request, id):
    if request.method == "POST":
        slot = Slot.objects.get(pk=id)
        slot.status = "available"
        slot.save()
        return redirect("/")
    
@csrf_protect
def bookParking(request, id):
    if request.method == "POST":
        slot = Slot.objects.get(pk=id)
        slot.status = "occupied"
        slot.save()
        return redirect("/")