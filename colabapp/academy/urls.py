from django.urls import path 
from .views import v_course

urlpatterns = [
    path('course/<int:course_id>', v_course)
]