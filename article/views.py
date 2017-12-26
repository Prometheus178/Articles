from article.forms import CommentForm
from django.shortcuts import render, redirect, render_to_response
from django.template import loader
from django.template import Context, Template
from django.http.response import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, Page
from django.contrib import auth

def basic_one(request):
    view = "basic_one"
    html = "<html><body> this is %s view </body></html>" %view
    return HttpResponse(html)

def template_two(request):

    my_dict = {'template_two': 'yellow'}
    my_template = 'мой любимый цвет {{ template_two }}'
    c = Context(my_dict)
    t =Template(my_template)
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)

def template_three_simple(request):
    name = 'template_three_simple'
    template = loader.get_template('article/myview.html')
    context = {
        'name': name,
    }
    return HttpResponse(template.render(context,request))

def articles(request,page_number = 1):

    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    args = {}
    args ['article'] = current_page.page(page_number)
    args ['username'] = auth.get_user(request).username
    return render_to_response('article/articles.html', args)

def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id = article_id)
    args['comments'] = Comments.objects.filter(comments_article_id = article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article/article.html', args)

def homepage(request):
    return render(request, 'article/homepage.html')
def zamena(request):
    return render(request, 'article/basic.html', {'zamena':['здесь мы подключили контент из бэйсика','1234567890']})
def addlike(request, article_id):
    try:
        article = Article.objects.get( id = article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id = article_id)
            form.save()
        return redirect('/article/get/%s/' % article_id)
