from django.urls import path
from .views import v_add_numbers, v_add_numbers2,add_student,student_list

urlpatterns = [
    
    path('add2/', v_add_numbers2, name='n_add_numbers2'),
    path('add/', v_add_numbers, name='n_add_numbers'),
    path('add3/', add_student, name='n_add_student'),
    path('alist/', student_list, name='n_student'),
]