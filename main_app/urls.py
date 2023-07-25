from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sonnyangels/', views.sonnyangels_index, name='index'),
]