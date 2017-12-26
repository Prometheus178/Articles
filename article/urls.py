from django.urls import include, path
from article import views


urlpatterns = [
    path('1/', views.basic_one, name='basic_one'  ),
    path('2/', views.template_two, name='template_two'),
    path('3/', views.template_three_simple, name='template_three_simple'),
    path('article/all/', views.articles, name='articles' ),
    path('', views.articles, name='articles' ),
    path('articles/get/<int:article_id>/', views.article, name='article' ),
    path('', views.homepage, name='homepage'),
    path('zamena/', views.zamena, name='zamena'),
    path('article/addlike/<int:article_id>/', views.addlike, name='addlike'),
    path('article/addcomment/<int:article_id>/', views.addcomment, name='addcomment'),
    path('page/<int:page_number>/', views.articles ),
    path('', views.articles),
]
