from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.form_employee, name="employee_insert"),
    path('<int:id>/',views.form_employee,name="employee_update"),
    path('delete/<int:id>',views.delete_employee,name='employee_delete'),
    path('list/',views.list_employee,name='employee_list'),
]
