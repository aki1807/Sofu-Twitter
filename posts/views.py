from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # 新しい順に並べる
    return render(request, "posts/home.html",{'posts': posts})

@login_required
def create(request):
     if request.method == "POST":
        title = request.POST.get("title")
        memo = request.POST.get("memo")
        
        # DBに保存
        Post.objects.create(title=title, memo=memo)

        return redirect("home")
     
     return render(request, "posts/create.html")