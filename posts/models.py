from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    content = models.CharField(max_length=280)  # 投稿内容（ツイート本文）
    created_at = models.DateTimeField(default=timezone.now)  # 投稿日時

    def __str__(self):
        return self.content[:20]  # 管理画面で最初の20文字だけ表示
