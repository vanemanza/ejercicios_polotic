from django.shortcuts import render

def vista1(request):

    return render(request, "webApp/vista1.html")


def vista2(request):
    
    return render(request, "webApp/vista2.html")

def vista3(request):
    
    return render(request, "webApp/vista3.html")

