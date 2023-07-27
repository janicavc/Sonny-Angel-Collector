from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sonnyangels/', views.sonnyangels_index, name='index'),
    path('sonnyangels/<int:sonnyangel_id>', views.sonnyangels_detail, name='detail'),
    path('sonnyangels/create/', views.SonnyCreate.as_view(), name='sonnyangels_create'),
    path('sonnyangels/<int:pk>/update/', views.SonnyUpdate.as_view(), name='sonnyangels_update'),
    path('sonnyangels/<int:pk>/delete/', views.SonnyDelete.as_view(), name='sonnyangels_delete'),   
    path('sonnyangels/<int:sonnyangel_id>/add_inspect/', views.add_inspect, name='add_inspect'),   
]