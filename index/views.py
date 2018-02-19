from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from .models import Post
from .forms import ImageForm
from .models import Images
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.forms import modelformset_factory

# Create your views here.
def Form(request):
    return render(request,"index/form.html", {})


def add(request):
    ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=2)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,queryset=Images.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image,)
                photo.save()
            messages.success(request,
                             "Yeeew,check it out on the home page!")

            return HttpResponseRedirect(post_form.get_absolute_url())
        else:
            print (postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'index/form.html',
                  {'postForm': postForm, 'formset': formset},)
def postdetail(request, id=None):
    instance_post = get_object_or_404(Post, id=id)
    all_images = Images.objects.filter(post=instance_post.id).order_by('-id')

    context={
        "title": instance_post.title,
        'image_list':all_images
    }
    return render(request, 'index/detail.html',context)
