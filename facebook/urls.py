
from django.contrib import admin
from django.urls import path
from users.views import posts, comments, likes, users


urlpatterns = [
    path('admin/', admin.site.urls),

    #   private
    path('my-posts/', posts.MyPostsApiView.as_view()),
    path('my-avg-posts/', posts.MyAvgPostsApiView.as_view()),


    #   public
    path('posts/', posts.PostsApiView.as_view()),

    #   Add
    path('comment-add/', comments.CommentAddApiView.as_view()),
    path('like-add/', likes.LikeAddApiView.as_view()),
    path('posts-add/', posts.PostsAddApiView.as_view()),
    # path('users-add/', users.UsersAddApiView.as_view()),
    path('users-add/', users.UserCreate.as_view(), name='add_user'),

]
