from django.shortcuts import render
from django.urls import reverse
from blog.models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import Logged_Super_User_Mixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Nuevas Views:

class Create_post(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'create_post.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('detail_post', kwargs={'pk':self.object.pk})

class Detail_post(DetailView):
    model = Note
    template_name = 'detail_post.html'

class Delete_post(Logged_Super_User_Mixin, DeleteView):
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

# Mostrar todas las notas:
class List_posts(ListView):
    model = Note
    template_name = 'bd.html'
    queryset = Note.objects.all()
#Buscador:
def search_note(request):
    notas = Note.objects.filter(title__icontains=request.GET['search'])
    context = {'notas': notas}
    return render(request, 'search_note.html', context = context)

#Views con noticias filtradas por categorías:

def entertainment_post(request):
    entertainment = Note.objects.filter(category_id = 1)
    context = {'entertainment' : entertainment}
    return render(request, 'entertainment_post.html', context = context)

def health_post(request):
    health = Note.objects.filter(category_id = 2)
    context = {'health' : health}
    return render(request, 'health_post.html', context = context)

def economy_post(request):
    economy = Note.objects.filter(category_id = 3)
    context = {'economy' : economy}
    return render(request, 'economy_post.html', context = context)

def sports_post(request):
    sports = Note.objects.filter(category_id = 4)
    context = {'sports' : sports}
    return render(request, 'sports_post.html', context = context)