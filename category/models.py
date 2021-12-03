from django.db import models

class Category(models.Model): # Таблица новостей которая наследует models.Model
    category_name = models.CharField(max_length=100) # название новости
    parent = models.ForeignKey('self',models.SET_NULL, unique=False, blank=True, null=True)
    
    class Meta:
    	verbose_name = ("Category") # человекочитаемое имя объекта
    	verbose_name_plural = ("Categories")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.category_name  # __str__ применяется для отображения объекта в интерфейсе

