from django.shortcuts import render, redirect
from Home.forms import CreateRecord
from Home.models import Record
from django.contrib import messages
# Create your views here.

def home(request):
    records = Record.objects.all()    
    context = {'records':records}
    return render(request, "Home/home.html", context)


def add_record(request):
    if request.method == "POST":
        form = CreateRecord(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record successfully created.")
            return redirect("/")

    else:
        form = CreateRecord()
    
    context = {'form':form}
    return render(request, "Home/create_record.html", context)


def modify_record(request, slug):
    record = Record.objects.get(uni_slug = slug)
    if request.method == "POST":
        form = CreateRecord(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated")
            return redirect("/")

    else:
        form = CreateRecord(instance=record)
    
    context = {'form':form}
    return render(request, "Home/modify_record.html", context)

def del_record(request, slug):
    record = Record.objects.get(uni_slug = slug)
    record.delete()
    messages.info(request, "Record Deleted.")
    return redirect("/")