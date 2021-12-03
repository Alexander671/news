from django.utils import timezone #мы будем получать дату создания todo
from django.db import models
from django.contrib.auth.models import User

from category.models import Category

class News(models.Model): # Таблица новостей которая наследует models.Model
    name = models.CharField(max_length=100) # название новости
    new_text = models.TextField(blank=False) # текст новости 
    date_of_create = models.DateField(auto_now_add=True) # дата создания
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
    	verbose_name = ("New") # человекочитаемое имя объекта
    	verbose_name_plural = ("News")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе

