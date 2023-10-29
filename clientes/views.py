from django.shortcuts import render, redirect
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
        

        #if name != "" and passwd != "":

        if acess_db:

            auth_acess = authenticate(request,username=name, password=passwd)
                
            if not auth_acess:
                    
                    
                user = User.objects.create_user(username=name)
                user.set_password(passwd)
                user.save()
                auth_acess = authenticate(request, username=name, password=passwd)

               
            if auth_acess is not None:
                login_system(request, auth_acess)

            return redirect('del_user')

        else:
            #return redirect('login')
            return render(request, 'login.html', {"error": "User not found"})
        
        #else:
            #return render(request, 'login.html', {"error": ""})
        #    return redirect('login')


    elif request.method == "GET":
    
        return render(request, 'login.html', {})



def create_user(request):

    if request.method == "POST":
        name = request.POST.get('name')
        passwd = request.POST.get('pass')
        db = Cliente.objects.filter(name=name)
        

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


def update_user(request):

    if request.user.is_authenticated and request.method == "POST":
        

        #name   = request.POST.get('name')
        passwd = request.POST.get('pass')
        email  = request.POST.get('email')
        number = request.POST.get('number')

        acess_db = Cliente.objects.get(name=get_user(request))
     
        if passwd:
            acess_db.password = passwd
        if email:
            acess_db.email = email
        if number:
            acess_db.number = number
        
        acess_db.save()
        
        return redirect('del_user')
        #return render(request, 'inside.html', {"msg_status": "Update successful"})

def del_user(request):


    if request.method == "POST":

        name   = request.POST.get('name')
        passwd = request.POST.get('pass')
        email  = request.POST.get('email')
        number = request.POST.get('number')

        acess_db = Cliente.objects.filter(name=str(get_user(request)))
        
        if acess_db: 
            acess_db.delete()
            logout(request)
            return render(request, 'inside.html', {"msg_status": "Remove successful"})
        else:
            return render(request, 'inside.html', {"msg_status": "User not found"})

    elif request.method == "GET":
        
        if request.user.is_authenticated:
           
            acess_db = Cliente.objects.filter(name=str(get_user(request)))
            
            return render(request, 'inside.html', {"msg_status": request.user, "name": acess_db[0].name,
                                                   "email": acess_db[0].email, "number": acess_db[0].number,
                                                    "pass": "**********" })
        
        else:
            return redirect('login')
            

