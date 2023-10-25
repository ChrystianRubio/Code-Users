from django.shortcuts import render
from .models import Cliente

# Create your views here.
def login(request):
    
    if request.method == "POST":

        name = request.POST.get('name')
        passwd = request.POST.get('pass')

        if name != "" and passwd != "":
            db = Cliente(name=name, password=passwd)
            
            db.save()
    
    elif request.method == "GET":
        db = Cliente.objects.all()
        
        print(db)
        
 
    return render(request, 'login.html')

    


