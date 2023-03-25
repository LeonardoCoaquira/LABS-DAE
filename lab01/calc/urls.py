from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:oper>/<int:num1>/<int:num2>/', views.calcular, name='calcular')
]