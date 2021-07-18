from django.shortcuts import render

def home(request):

    return render(request, "webApp/home.html")

def productos(request):

    return render(request, "webapp/productos.html")

def contacto(request):

    return render(request, "webApp/contacto.html")    


