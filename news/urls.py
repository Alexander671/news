
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from django.conf.urls import url

from news_news.views import news #   , news_id
from category.views import category, thanks
from tags.views import tags
from autors.views import autors
from drafts.views import drafts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    url('news/', news, name="News"),
    url('category/', category, name="Category"),
 	url('tags/', tags, name = 'tags'),
    url('drafts/', drafts, name = 'Drafts'),
    url('autors/', autors, name = 'Autors'),
    url('thanks/', thanks, name = 'Thanks')
] 