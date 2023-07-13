from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def v_index(request):
    context = {
        'course1': Course.objects.get(name = 'Matematica Avanzada'),
        'course2': Course.objects.get(name = 'Literatura')
    }
    return render(request, 'index.html', context)
    #enlaza el view con el html 

def v_course(request, course_id):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    return render(request, 'course.html', context)

@login_required(login_url = "/admin/login")
@permission_required('academy.add_subscribe', login_url = "/admin/login")
def v_subscribe(request, course_id):
    pass
    

    