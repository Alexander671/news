from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import Tags
from django.forms import formset_factory
from .form import TagsForm
from django.forms import modelformset_factory
from itertools import chain


def tags(request):
    TagFormSet = modelformset_factory(Tags, fields=('tag_name',))
    tags = Tags.objects.all()
    tags_formset = formset_factory(TagsForm)
    formset = tags_formset()
    if request.method == 'POST':
        form = TagFormSet(request.POST)
    
        # check whether it's valid:
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/tags/')
        else:
            error_list = chain.from_iterable(map(lambda x: x.values(), form.errors))
            return render(request, 'tags/tags.html', {'tags':tags, 'formset' : formset, 'errors' : error_list})

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'tags/tags.html', {'tags':tags, 'formset' : formset})
def thanks(request):
    return HttpResponse("Thanks for being awesome!")