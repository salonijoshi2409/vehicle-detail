from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import Vechicleform
from .models import Vechicle
from django.contrib import messages
# Create your views here.
def adddata(request):
    if request.method == 'POST':
        vech = Vechicleform(request.POST)
        if vech.is_valid():
            vech.save()
            messages.add_message(request, messages.SUCCESS, 'Vehicle added!!')
            return HttpResponseRedirect('/add/')
    else:
        vech= Vechicleform()
    return render(request,'addvehicle.html', {'vech': vech})

def listdata(request):
    vehicles= Vechicle.objects.order_by('-id').all()
    return render(request,'listvehicle.html',{'vehicles': vehicles})

def deletedata(request, id):
    if request.method == 'POST':
        li = Vechicle.objects.get(pk=id)
        li.delete()
        return HttpResponseRedirect('/')

def updatedata(request, id):
    if request.method == 'POST':
        li = Vechicle.objects.get(pk=id)
        vech = Vechicleform(request.POST, instance=li)
        if vech.is_valid():
            vech.save()
            messages.add_message(request, messages.SUCCESS, 'Vehicle updated!!')
    else:
        li = Vechicle.objects.get(pk=id)
        vech = Vechicleform(instance=li)
    return render(request,'addvehicle.html', {'vech': vech})

def detaildata(request,id):
    if request.method == 'POST':
        if request.POST.get("on"):
            up = Vechicle.objects.get(pk=id)
            up.on_off = True
            print(up.on_off)
            up.save()
        if request.POST.get("off"):
            up = Vechicle.objects.get(pk=id)
            up.on_off = False
            up.save()
    li = Vechicle.objects.get(pk=id)
    return render(request,'detailvehicle.html',{'li': li})