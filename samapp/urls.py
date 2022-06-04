from django.urls import path
from samapp import views
# from views import image_upload_view
urlpatterns = [ 
    path('', views.index, name='index'),
    path('upload/', views.image_upload_view, name='image_upload_view'),
    path('extract/', views.data_extract_view, name='data_extract_view'),
]