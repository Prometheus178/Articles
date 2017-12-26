
from django.db import models
from django.utils.encoding import smart_text

class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = models.CharField(default='', max_length=200)
    article_text = models.TextField(blank=True, default='')
    article_date = models.DateTimeField(default='')
    article_likes = models.IntegerField(default=0)
    def _str_(self):
        return smart_text(self.article_tittle)

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(blank=True, default='',verbose_name='Текст комментария')
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
