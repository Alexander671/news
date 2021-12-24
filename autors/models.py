from django.db import models
from django.conf import settings

class Autors(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    description = models.TextField()
    class Meta:
        verbose_name = ("Autor") # человекочитаемое имя объекта
        verbose_name_plural = ("Autors")  #человекочитаемое множественное имя
    def __str__(self):
        return str(self.user)  # __str__ применяется для отображения объекта в интерфейсе

