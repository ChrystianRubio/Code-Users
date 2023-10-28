from django.shortcuts import render
from .models import Cliente
from django.contrib.auth import authenticate, get_user, logout
from django.contrib.auth import login as login_system
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    
    
    if request.method == "POST":

        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        
        acess_db = Cliente.objects.filter(name=name, password=passwd)
        

        if name != "" and passwd != "":

            if acess_db:

                auth_acess = authenticate(request,username=name, password=passwd)
                
                if not auth_acess:
                    print("autho acess>>>>> ", auth_acess)
                    
                    user = User.objects.create_user(username=name)
                    user.set_password(passwd)
                    user.save()
                    auth_acess = authenticate(request, username=name, password=passwd)

               
                if auth_acess is not None:
                    login_system(request, auth_acess)

                return render(request, 'inside.html', {"name": name, "pass": passwd, 
                                                        "email": str(acess_db[0].email), "number": str(acess_db[0].number)})
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


    if request.method == "POST":

        name   = request.POST.get('name')
        passwd = request.POST.get('pass')
        email  = request.POST.get('email')
        number = request.POST.get('number')

        acess_db = Cliente.objects.filter(name=name, password=passwd)
        
        if acess_db: 
            acess_db.delete()
            logout(request)
            return render(request, 'inside.html', {"msg_status": "Remove successful"})
        else:
            return render(request, 'inside.html', {"msg_status": "User not found"})

    elif request.method == "GET":
        
        if request.user.is_authenticated:
            print(f'request.user>>> {get_user(request)}')
            return render(request, 'inside.html', {"msg_status": request.user})
        
        else:
            return render(request, 'login.html', {"msg_status": ""})

