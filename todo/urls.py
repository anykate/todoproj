from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addToDo, name='add'),
    path('complete/<int:todo_id>/', views.completeToDo, name='complete'),
    path('deletecompleted/', views.deleteCompleted, name='deletecompleted'),
    path('deleteall/', views.deleteAll, name='deleteall'),
]
