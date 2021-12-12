from django.db import models
from django.conf import settings

class Autors(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    description = models.TextField()
    class Meta:
        verbose_name = ("Autor") # человекочитаемое имя объекта
        verbose_name_plural = ("Autors")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе

