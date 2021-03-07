from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find_donar/', views.find_donar, name='find_donar'),
    path('new_donar/', views.new_donar, name='new_donar'),
]