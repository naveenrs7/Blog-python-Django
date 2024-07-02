from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.

#static demo data
# posts=[
#         {'id': 1, 'title': 'Post 1', 'content': 'This is the content of post 1', 'catagory': 'Sports'},
#         {'id': 2, 'title': 'Post 2', 'content': 'This is the content of post 2', 'catagory': 'Design'},
#         {'id': 3, 'title': 'Post 3', 'content': 'This is the content of post 3', 'catagory': 'Architecture'},
#         {'id': 4, 'title': 'Post 4', 'content': 'This is the content of post 4', 'catagory': 'History'},
#         {'id': 5, 'title': 'Post 5', 'content': 'This is the content of post 5', 'catagory': 'Politics'},
#         {'id': 6, 'title': 'Post 6', 'content': 'This is the content of post 6', 'catagory': 'Country'},
#     ]

def index(request):
    blog_title = "Latest Posts"
    
    # getting data from post model
    all_posts = Post.objects.all()


    # paginate
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blog/index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def detail(request,slug):

    # static data
    # post = next((i for i in posts if i['id'] == post_id),None)
  
    # getting data from model by post id
    post = Post.objects.get(slug = slug)
    related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    return render(request,'blog/detail.html', {'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("You are viewing new URL")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            success_message = "Youe Email has been sent"
            return render(request,'blog/contact.html',{'form':form, 'success_message':success_message})

        return render(request,'blog/contact.html',{'form':form, 'name':name, 'email':email, 'message':message})
    return render(request,'blog/contact.html')


def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})
