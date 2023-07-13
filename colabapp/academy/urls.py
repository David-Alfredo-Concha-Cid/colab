from django.urls import path 
from .views import v_course, v_subscribe

urlpatterns = [
    path('course/<int:course_id>', v_course),
    path('course/<int:course_id>/subscribe', v_subscribe)
]