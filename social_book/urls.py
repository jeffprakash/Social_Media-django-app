
from django.conf.urls.static import static
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.views import View

from Social_media import settings
from . import views


urlpatterns=[

    path('',views.index,name='index'),
    path('settings',views.settings,name='settings'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout')

]
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)