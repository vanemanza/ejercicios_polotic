from django.shortcuts import render

def home(request):

    return render(request, "webApp/home.html")


def vista2(request):
    
    return render(request, "webApp/vista2.html")

def vista3(request):
    
    return render(request, "webApp/vista3.html")

