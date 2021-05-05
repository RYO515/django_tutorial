from django.contrib import admin
from django.urls import path
from blog.views import PostDetailView, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'posts/<int:post_id>',
        PostDetailView.as_view(),
        name="post_detail"
    ),
    path(
        '',
        PostListView.as_view(),
        name="post_list"
    ),
]
