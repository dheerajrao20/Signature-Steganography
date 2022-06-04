from django.shortcuts import render
from .forms import ImageForm, ImageExt
import cv2
import string
import os

def img_names(dir_path):
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res


def index(request):
    
    return render(request, 'index.html')


    
def image_upload_view(request):
    """Process images uploaded by users"""

    # -----------------
    dir_path = r'.//media//images//'
    res=img_names(dir_path)

    for i in range(0, len(res)):
        os.remove(dir_path + res[i])

    res.clear()
    # -----------------

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            password = form.cleaned_data['Password']
            data = form.cleaned_data['Data']
            # =======
            d = {}
            c = {}

            for i in range(255):
                d[chr(i)] = i
                c[i] = chr(i)


            # ---------------------- 
            res=img_names(dir_path)
            # -----------------------
            img_name=res[0]
            x = cv2.imread("./media/images/"+img_name)
            
            i = x.shape[0]
            j = x.shape[1]

            key = password
            text = data

            kl = 0
            tln = len(text)

            z=0
            n=0
            m=0
            l=len(text)

            for i in range(l):
                x[n,m,z]=d[text[i]]^d[key[kl]]
                n=n+1
                m=m+1
                m=(m+1)%3
                kl=(kl+1)%len(key)

            cv2.imwrite("encrypted_img.jpg",x) 
# ----------------------------------------------------- 
            os.startfile("encrypted_img.jpg")

            kl =0
            tln = len(text)
            z=0
            n=0
            m=0

            decrypt=""
            for i in range(l):
                decrypt+=c[x[n,m,z]^d[key[kl]]]
                n=n+1
                m=m+1
                m=(m+1)%3
                kl=(kl+1)%len(key)

            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload.html', { 'img_obj': img_obj,'data':data})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})





def data_extract_view(request):
    if request.method == 'POST':
        form = ImageExt(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            password2 = form.cleaned_data['Password2']

            img_obj = form.instance
            return render(request, 'extract.html', {'form': form, 'img_obj': img_obj, 'password2':password2,})
    else:
        form = ImageForm()
    # return render(request, 'upload.html', {'form': form})

    return render(request, 'extract.html', {'form':form})