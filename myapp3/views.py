from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from .models import Author, Post


def hello(request):
    return HttpResponse('Hello 1')


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello 2")


def year_post(request, year):
    text = ""
    ...  # Формируем статьи за год
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # Формируем статьи за год и месяц
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'Какой-то Title',
        'content': 'Какой-то content'
    }
    return JsonResponse(post, json_dumps_params={
        'ensure_ascii': False})  # {'ensure_ascii': False} - используется, если в передаваемой объекте используется не только символы ascii, но и все символы utf-8


def my_view(request):
    context = {'name': "John"}
    return render(request, 'myapp3/index.html', context)


class TemplIf(TemplateView):
    template_name = 'myapp3/templ_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Привет всем!!!!'
        context['number'] = 4
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'желтый',
        'знать': 'зеленый',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/temple_for.html', context)


def index(request):
    return render(request, 'myapp3/index_base.html')


def about(request):
    return render(request, 'myapp3/about_base.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5] #('-id')[:5] - фильтр в обратном порядке от большого id к меньшему и вывод 5 записей с самого начала, т.е 5 самых старых записей с самыми большими id
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
