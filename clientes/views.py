from django.shortcuts import render
from .models import Cliente
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    
    
    if request.method == "POST":

        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        
        acess_db = Cliente.objects.filter(name=name, password=passwd)


        if name != "" and passwd != "":

            if acess_db:
                authenticate(username=name, password=passwd)

                return render(request, 'inside.html', {"name": name})
            
            else:
                return render(request, 'login.html', {"error": "User not found"})
        
        else:
            return render(request, 'login.html', {"error": ""})


    elif request.method == "GET":
    
        return render(request, 'login.html', {})



def create_user(request):

    if request.method == "POST":
        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        db = Cliente.objects.filter(name=name, password=passwd)
        

        if name != "" and passwd != "":
            
            if not db:
                acess_db = Cliente(name=name, password=passwd)
                acess_db.save()
                return render(request, 'register.html', {"msg_status": "Registration successful "})
            else:
                return render(request, 'register.html', {"msg_status": "User already exist."})
        
        else:
            return render(request, 'register.html', {})



    elif request.method == "GET":
        return render(request, 'register.html', {})


def del_user(request):

    print(request)

    if request.method == "POST":

        name = request.POST.get('name')
        passwd = request.POST.get('pass')

        acess_db = Cliente.objects.filter(name=name, password=passwd)
        
        if acess_db: 
            acess_db.delete()
            return render(request, 'inside.html', {"msg_status": "Remove successful"})
        else:
            return render(request, 'inside.html', {"msg_status": "User not found"})

    elif request.method == "GET":
        
        if request.user.is_authenticated:
            return render(request, 'inside.html', {"msg_status": ""})
        
        else:
            return render(request, 'login.html', {"msg_status": ""})

