
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.views.generic.base import TemplateView # new
from news_news.views import news, redirect_view
from category.views import category, thanks
from tags.views import tags
from autors.views import Autors, delete
from drafts.views import Drafts
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_view),
    re_path('news/', news, name="News"),
    re_path('category/', category, name="Category"),
 	re_path('tags/', tags, name = 'Tags'),
    url('drafts/', Drafts.as_view(), name = 'Drafts'),
    url('autors/', Autors.as_view(), name = 'Autors'),
    re_path('autor_delete/', delete , name = 'Delete'),
    re_path('thanks/', thanks, name = 'Thanks')
] 

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)