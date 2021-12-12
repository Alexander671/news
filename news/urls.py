
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.views.generic.base import TemplateView # new
from news_news.views import news, redirect_view
from category.views import category, thanks
from tags.views import tags
from autors.views import autors
from drafts.views import drafts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_view),
    re_path('news/', news, name="News"),
    re_path('category/', category, name="Category"),
 	re_path('tags/', tags, name = 'Tags'),
    re_path('drafts/', drafts, name = 'Drafts'),
    re_path('autors/', autors, name = 'Autors'),
    re_path('thanks/', thanks, name = 'Thanks')
] 