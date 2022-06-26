from turtle import update
from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('indexX',views.indexX,name='indexX'),
    path('',views.login,name='login'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('adlogout',views.adlogout,name='adlogout'),
    path('RegForm',views.RegForm,name='RegForm'),
    path('regdisplay',views.regdisplay,name='regdisplay'),
    path('REG',views.REG,name='REG'),
    path('Cdisplay',views.Cdisplay,name='Cdisplay'),
    path('Cedit/<int:eid>/',views.Cedit,name='Cedit'),
    path('Cupdate/<int:uid>/',views.Cupdate,name='Cupdate'),
    path('Cdelete/<int:did>/',views.Cdelete,name='Cdelete'),
    path('EditR',views.EditR,name='EditR')

]