from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post 
# Create your views here.
class BlogPostView(ListView):
    model=Post
    template_name='home.html'
class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']
    # success_url=reverse_lazy('home')  # biz shunday qilsak ham togri bu sood qiyini [models.py da]p
class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')