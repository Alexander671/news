from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Category
from django.forms import formset_factory
from .form import CategoryForm
from django.forms import modelformset_factory
def category(request):
    CategoryFormSet = modelformset_factory(Category, fields=('parent', 'category_name'))
    if request.method == 'POST':
        form = CategoryFormSet(request.POST)
        # check whether it's valid:
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            return HttpResponse('something went wrong' )
    # if a GET (or any other method) we'll create a blank form
    else:
        category = Category.objects.all()
        category_formset = formset_factory(CategoryForm)
        formset = category_formset()
        return render(request, 'category/category.html', {'categories':category, 'formset' : formset})
def thanks(request):
    return HttpResponse("Thanks for being awesome!")