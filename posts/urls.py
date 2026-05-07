from django.urls import path
from SofuTwitter.posts import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
]