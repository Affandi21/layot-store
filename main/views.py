from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import LayotStoreForm
from main.models import LayotStore

def show_main(request):
    to_cart = LayotStore.objects.all()

    context = {
        'name': 'Old Book',
        'price': 'Rp259.000,00',
        'description': 'Old book found in my backyard',
        'to_cart': to_cart
    }

    return render(request, "main.html", context)

def add_to_cart(request):
    form = LayotStoreForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_to_cart.html", context)

def show_xml(request):
    data = LayotStore.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = LayotStore.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = LayotStore.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = LayotStore.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")