from django.shortcuts import render, redirect
from .models import Post
from .ai_check import check_politeness

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "posts/home.html", {'posts': posts})

# 投稿画面
def create(request):
    error_message = None

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # AI判定を実行
            is_polite, reason = check_politeness(content)

            if is_polite:
                # 保存してホーム
                Post.objects.create(content=content, memo = reason)
                return redirect('home')
            else:
                #エラーメッセージを出して、そのまま投稿画面に留まる
                error_message = reason

    return render(request, "posts/create.html", {'error_message': error_message})
