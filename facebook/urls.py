"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
# from users.views import PostResumen, LikeTotal
from users.views2 import PostResumen, LikeTotal
from users.views import posts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', PostResumen.as_view()),
    path('like2/', LikeTotal.as_view()),

    #   private
    path('my-posts/', posts.MyPostsApiView.as_view()),
    path('my-avg-posts/', posts.MyAvgPostsApiView.as_view()),


    #   public
    path('posts/', posts.PostsApiView.as_view()),



]
