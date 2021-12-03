from django.db import models

class Tags(models.Model): # Таблица новостей которая наследует models.Model
    tag_name = models.CharField(max_length=100, unique = True) # название тега
    class Meta:
    	verbose_name = ("Tag") # человекочитаемое имя объекта
    	verbose_name_plural = ("Tags")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.tag_name  # __str__ применяется для отображения объекта в интерфейсе

