from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
  title = models.CharField('Заголовок', max_length=200)
  content = RichTextField('Содержание', config_name='default')
  created_at = models.DateTimeField('Дата создания', auto_now_add=True)
  is_published = models.BooleanField('Опубликовано', default=True)
  
  class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'
    ordering = ['-created_at']
  
  def __str__(self):
    return self.title