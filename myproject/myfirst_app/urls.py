from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hi/', views.hi, name='hi'),
    path('see/', views.see_page, name='see'),
    path('learn_more/', views.learn_more_page, name='learn_more'),
]
