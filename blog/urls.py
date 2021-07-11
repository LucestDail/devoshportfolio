from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog/', blog_main),
    path('blog/post/', blog_post),
    path('blog/post/<category>/', blog_post_category),
    path('blog/<int:pk>/', blog_post_view)
]