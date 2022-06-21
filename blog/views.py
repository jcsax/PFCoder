from turtle import title
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from blog.models import Note
from blog.forms import Note_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Nuevas Views:

class List_posts(ListView):
    model = Note
    template_name = 'bd.html'
    queryset = Note.objects.all()

class Create_post(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'create_post.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('detail_post', kwargs={'pk':self.object.pk})

class Detail_post(DetailView):
    model = Note
    template_name = 'detail_post.html'


class Delete_post(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'delete_post.html'
    def get_success_url(self):
        return reverse('list_posts')


class Update_post(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'update_post.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('detail_post', kwargs = {'pk':self.object.pk})

def search_note(request):
    notas = Note.objects.filter(title__icontains=request.GET['search'])
    context = {'notas': notas}
    return render(request, 'search_note.html', context = context)
