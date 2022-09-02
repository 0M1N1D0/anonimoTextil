
from django.urls import path, include
from .views import homepageView


homepage_urlpatterns = [

    path('', homepageView, name='homepage'),
]