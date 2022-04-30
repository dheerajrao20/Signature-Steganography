from django.urls import path
from mainapp import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('download', views.download, name='download'),
]