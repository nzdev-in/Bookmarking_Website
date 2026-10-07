from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/create.html',{'section':'images','form':form})

def imageDetail(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)
    return render(request,'images/detail.html',{'section':'images' , 'image':image})