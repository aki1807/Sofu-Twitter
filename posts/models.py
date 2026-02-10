from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20] 
