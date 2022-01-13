from django.db import models
from django.conf import settings

class DraftsModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    text = models.TextField()
    images = models.ImageField(upload_to = 'images/' ,null = True)
    class Meta:
        verbose_name = ("Draft") # человекочитаемое имя объекта
        verbose_name_plural = ("Drafts")  #человекочитаемое множественное имя
    def __str__(self):
        return str(self.user)  # __str__ применяется для отображения объекта в интерфейсе
