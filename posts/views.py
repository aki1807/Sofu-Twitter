from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # 新しい順に並べる
    return render(request, "posts/home.html",{'posts': posts})