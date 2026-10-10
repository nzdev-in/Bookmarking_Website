from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import HttpResponse
from actions.utils import create_action


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            create_action(request.user,"bookmarked",new_image)
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/create.html',{'section':'images','form':form})

def imageDetail(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)
    return render(request,'images/detail.html',{'section':'images' , 'image':image})



@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            img = Image.objects.get(id=image_id)
            if action == 'like':
                img.users_like.add(request.user)
                create_action(request.user,'liked',img)
            else:
                img.users_like.remove(request.user)
            html = render_to_string(
                'images/users_liked.html',
                {'image':img},
                request=request
            )
            return JsonResponse({'status':'ok',
                                 'id':image_id,
                                 'action':action,
                                 'user_like_html':html})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status':'error'})  

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request,'images/image_list.html',{'section':'images',
                                                        'images':images})
    return render(request,'images/list.html',{'section':'images',
                                              'images':images})

