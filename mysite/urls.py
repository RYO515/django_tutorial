from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/<int:post_id>', post_detail, name="post_detail"),
    path('', post_list, name="post_list"),
]
