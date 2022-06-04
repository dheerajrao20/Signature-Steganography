from django.urls import path
from f_extract import views
# from views import image_upload_view
urlpatterns = [ 
    path('extract/', views.extract, name='extract'),
]