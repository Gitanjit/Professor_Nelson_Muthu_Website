from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home, teaching, projectpg, publicationpg, projview

urlpatterns = [
    path('', home),
    path('teaching/', teaching),
    path('projects/', projectpg),
    path('publications/', publicationpg),
    path('<int:id>/', projview, name='projdetail'),
    path('projects/<int:id>/', projview, name='projdetail')
]