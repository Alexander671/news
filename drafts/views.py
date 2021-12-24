from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import View

from drafts.form import DraftsForm
from drafts.models import DraftsModel

class Drafts(View):
    def get(self, request):
        form = DraftsForm()
        drafts = DraftsModel.objects.all()
        is_autor = drafts.filter(user_draft = request.user.id)
        return render(request, 'drafts/drafts.html', {'drafts' : drafts, 'is_autor' : is_autor, 'formset': form})

    def post(self, request):
        form = DraftsForm(request.POST)
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.user_draft = request.user
            profile.save()

            return redirect('/thanks/')
        return render(request, 'drafts/drafts.html', {'formset': form})


def delete(request):
        instance = DraftsModel.objects.filter(user_draft=request.user)
        instance.delete()
        return HttpResponse("Deleted!")
