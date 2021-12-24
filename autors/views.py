from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import redirect, render
from autors.form import AutorForm

from autors.models import Autors as Autor

class Autors(View):
    def get(self, request):
        form = AutorForm()
        autors = Autor.objects.all()
        is_autor = autors.filter(user_id = request.user.id)
        return render(request, 'autors/autors.html', {'autors' : autors, 'is_autor' : is_autor, 'formset': form})

    def post(self, request):
        form = AutorForm(request.POST)
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('/thanks/')
        return render(request, 'autors/autors.html', {'formset': form})


def delete(request):
        instance = Autor.objects.filter(user_id=request.user)
        instance.delete()
        return HttpResponse("Deleted!")

def thanks(request):
    return HttpResponse("Thanks for being awesome!")