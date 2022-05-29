from django.urls import path
from samapp import views
# from views import image_upload_view

urlpatterns = [ 
    path('', views.image_upload_view, name='image_upload_view'),
]