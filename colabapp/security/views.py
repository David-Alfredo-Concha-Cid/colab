from django.shortcuts import render
from security.forms import StudentForm
from django.contrib.auth.models import Permission
# Create your views here.

def v_signup(request):
    if request.method == 'POST':
        data = request.POST.copy() #tmo todos los datoas del frontend
        data['username'] = data['email'] #alteramos previamente
        
        form = StudentForm(data) #comparo con el backend
        if form.is_valid(): # valido
            us = form.save() #se guarda en base de datos, creando el registro

            us.is_staff = True #doy mas capacidades a ese registo de db
            us.is_active = True #doy mas capacidades a ese registo de db
            us.set_password(data['password']) # se cifra la contraseña
            us.save() # se vuelve a guardar en bd para actualizar en db
            perm = Permission.objects.get(name = "Can add subscription")
            us.user_permissions.add(perm) #asignamos permiso
        
        else:
            print(">>", form.errors)



    context = {}
    return render(request, 'signup.html', context)
    


