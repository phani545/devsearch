from django.urls import path
from . import views

urlpatterns= [
    path('',views.projects,name='projects'),
    path('projectadd/<str:pk>/',views.project,name='project'),
    path('create_Project/',views.create_Project,name='create_Project'),
    path('update_Project/<str:pk>/',views.update_Project,name='update_Project'),
    path('delete_Project/<str:pk>/',views.delete_Project,name='delete_Project'),
]