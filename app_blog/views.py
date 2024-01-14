from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse

from app_blog.forms import BlogpostForm
from app_blog.models import Blogpost

from app_mailing.views import BaseContextMixin


# Create your views here.


class BlogpostListView(BaseContextMixin, ListView):
    model = Blogpost
    extra_context = {
        'title': 'Публикации'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogpostCreateView(BaseContextMixin, CreateView):
    model = Blogpost
    form_class = BlogpostForm
    success_url = reverse_lazy('app_blog:post_list')

    extra_context = {
        'title': 'Создание публикации'
    }


class BlogpostDetailView(BaseContextMixin, DetailView):
    model = Blogpost
    extra_context = {
        'title': 'Публикация'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogpostUpdateView(BaseContextMixin, UpdateView):
    model = Blogpost
    form_class = BlogpostForm
    # success_url = reverse_lazy('app_blog:post_view')

    extra_context = {
        'title': 'Редакция публикации'
    }

    def get_success_url(self):
        return reverse('app_blog:post_view', args=[self.object.pk])


class BlogpostDeleteView(BaseContextMixin, DeleteView):
    model = Blogpost
    success_url = reverse_lazy('app_blog:post_list')

    extra_context = {
        'title': 'Удаление публикации'
    }
