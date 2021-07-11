"""devosh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import main_index
from blog.views import blog_main, blog_post, blog_post_category, blog_post_view
from portfolio.views import portfolio_main
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #main
    path('', main_index, name='index'),

    #blog
    path('blog/', blog_main, name='blog_main'),
    path('blog/post/', blog_post, name='blog_post'),
    path('blog/post/<category>/', blog_post_category, name='blog_post_category'),
    path('blog/<int:pk>/', blog_post_view, name='blog_post_view'),
    #portfolio
    path('portfolio/', portfolio_main, name='portfolio_main')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
