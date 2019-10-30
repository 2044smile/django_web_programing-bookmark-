from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Bookmark
# Create your views here.


class BookmarkList(ListView):
    model = Bookmark
    paginate_by = 2


class BookmarkCreate(CreateView):
    model = Bookmark
    fields = '__all__' # ['site_name', 'site_url'] '__all__'로 가능
    success_url = reverse_lazy('list') # urls.py name을 찾아간다.


class BookmarkDetail(DetailView):
    model = Bookmark


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'site_url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = reverse_lazy('list')