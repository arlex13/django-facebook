from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
# models
from .models.comments import Comment

from .models.likes import Like

from .models.likes import Post
# # forms
# from .forms import EmpleadoForm


class PostResumen(ListView):
    template_name = 'posts.html'
    context_object_name = 'dato_enviado'

    def get_queryset(self):
        comentarios = Comment.objects.filter(post__id=2)
        return comentarios


class LikeTotal(ListView):
    template_name = 'likes.html'
    context_object_name = 'dato_enviado'

    def get_queryset(self):

        tota_like = Like.objects.filter(like=True, post__id=2).count()
        total_no_like = Like.objects.filter(like=False, post__id=2).count()
        post = Post.objects.get(id=2)
        enviar = (tota_like, total_no_like, post)
        return enviar
