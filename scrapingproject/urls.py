from django.contrib import admin
from django.urls import path
from scrappy.views import *




urlpatterns = [

    path('admin/', admin.site.urls),
    path('scrap/',ScrapDataView.as_view(),name='scrap'),
    ]