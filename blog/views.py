from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entertainment, Health, Economy
from blog.forms import Economy_form, Health_form, Entertainment_form

# Create your views here.
def post_entertainment(request):
    post_entertainment = Entertainment.objects.all()
    context = {'post_entertainment': post_entertainment}
    return render(request, 'post_entertainment.html', context=context)

def post_health(request):
    post_health = Health.objects.all()
    context = {'post_health': post_health}
    return render(request, 'post_health.html', context=context)

def post_economy(request):
    post_economy = Economy.objects.all()
    context = {'post_economy': post_economy}
    return render(request, 'post_economy.html', context=context)

def create_post_health(request):
    if request.method == 'GET':
        form = Health_form()
        context = {'form':form}
        return render(request, 'create_post_health.html', context=context)
    else:
        form = Health_form(request.POST)
        if form.is_valid():
            new_post_health = Health.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_post_health':new_post_health}
        return render(request, 'create_post_health.html', context=context)

def create_post_economy(request):
    if request.method == 'GET':
        form = Economy_form()
        context = {'form':form}
        return render(request, 'create_post_economy.html', context=context)
    else:
        form = Economy_form(request.POST)
        if form.is_valid():
            new_post_economy = Economy.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_post_economy':new_post_economy}
        return render(request, 'create_post_economy.html', context=context)

def create_post_entertainment(request):
    if request.method == 'GET':
        form = Entertainment_form()
        context = {'form':form}
        return render(request, 'create_post_entertainment.html', context=context)
    else:
        form = Entertainment_form(request.POST)
        if form.is_valid():
            new_post_entertainment = Entertainment.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_post_entertainment':new_post_entertainment}
        return render(request, 'create_post_entertainment', context=context)

def search_note(request):
    print(request.GET)
    entertainment = Entertainment.objects.filter(title__icontains = request.GET['search'])
    economy = Economy.objects.filter(title__icontains = request.GET['search'])
    health = Health.objects.filter(title__icontains = request.GET['search'])
    context = {'entertainment': entertainment, 'economy': economy,'health':health}
    return render(request, 'search_note.html', context = context)
