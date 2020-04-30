from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    posts = Post.objects.latest('date_created')

    posts_last = Post.objects.order_by('-id')[1:10]

    context = {'posts': posts, 'posts_last': posts_last}
    return render(request, 'blog/index.html', context)


def new_post(request):
    form = PostForm
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}

    return render(request, 'blog/new_post.html', context)