from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
<<<<<<< HEAD

def post_list(request):
    return render(request, 'blog/post_list.html', {})
=======
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
>>>>>>> fc6d63c5ed32e26826c5adb0f371a483621e73a3
