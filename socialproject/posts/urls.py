from django.urls import path
from . import views


urlpatterns = [
    path('feed/',views.feed,name ='index'),
    path('create/',views.post_create,name ='create'),
]
