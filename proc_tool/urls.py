from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]
