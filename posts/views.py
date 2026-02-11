from django.shortcuts import render, redirect
from .models import Post
from .ai_check import check_politeness

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "posts/home.html", {'posts': posts})

def create(request):
    error_message = None

    if request.method == 'POST':
        content = request.POST.get('content')
        print(content)
        if content:
            is_polite, reason = check_politeness(content)

            if is_polite:
                Post.objects.create(content=content)
                return redirect('home')
            else:
                error_message = reason

    return render(request, "posts/create.html", {'error_message': error_message})
