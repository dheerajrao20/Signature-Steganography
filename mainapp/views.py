
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        image1 = request.POST['file1']
        return image1

    return render(request, 'upload.html')

def download(request, image1):
    return render(request ,'download.html', {'image1':image1})
