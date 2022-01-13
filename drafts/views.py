from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import View

from drafts.form import DraftsForm
from drafts.models import DraftsModel
from autors.models import Autors


class Drafts(View):
    def get(self, request):
        form = DraftsForm()
        drafts = DraftsModel.objects.filter(user = request.user)
        is_autor = Autors.objects.filter(user = request.user.id)
        return render(request, 'drafts/drafts.html', {'drafts' : drafts, 'is_autor' : is_autor, 'formset': form})

    def post(self, request):
        form = DraftsForm(request.POST, request.FILES)
        if form.is_valid():
            
            draft = form.save(commit=False)
            draft.user = request.user
            draft.save()

            return redirect('/thanks/')
        return render(request, 'drafts/drafts.html', {'formset': form})


def delete(request):
        instance = DraftsModel.objects.filter(user=request.user)
        instance.delete()
        return HttpResponse("Deleted!")
