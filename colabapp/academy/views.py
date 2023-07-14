from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Course, Subscription, Subject
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
@permission_required('academy.add_subscription', login_url = "/admin/login")
def v_subscribe(request, course_id):
    #traer el ultimo subject del curso
    subject = Subject.objects.filter(course_id = course_id).last()
    if subject is None:
        messages.error(request, "No puedes susbcribirte a este curso.")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))
    #filter es un where course_id = 12 and student =33

    verificar = Subscription.objects.filter(subject_id = subject.id, student_id = request.user.id)
    if verificar.exists():
        messages.success(request, "Tu suscripcion ya esta activa.")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))
    else:
        subs = Subscription()
        subs.student_id = request.user.id
        subs.subject_id = subject.id
        subs.course_id = course_id
        subs.save()
        messages.success(request, "En buena hora, acabas de suscribirte!")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))



    