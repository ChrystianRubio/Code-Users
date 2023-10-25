from django.shortcuts import render
from .models import Cliente

# Create your views here.
def login(request):
    
    if request.method == "POST":

        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        acess_db = Cliente.objects.filter(name=name, password=passwd)


        if name != "" and passwd != "":
            if acess_db:
                return render(request, 'inside.html', {})
            else:
                return render(request, 'login.html', {})

   
    
    elif request.method == "GET":
    
        return render(request, 'login.html', {})


def inside_form(request):
    return render(request, 'inside.html', {})


