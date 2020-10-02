from django.urls import path
from django.shortcuts import reverse
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<int:pk>', views.post, name='post'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('create', views.PostCreate.as_view(), name='create'),
    path('update/<int:pk>', views.updatePost, name='update'),
]
