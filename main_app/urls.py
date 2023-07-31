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
    path('sonnyangels/<int:sonnyangel_id>/assoc_outfit/<int:outfit_id>/', views.assoc_outfit, name='assoc_outfit'),
    path('sonnyangels/<int:sonnyangel_id>/assoc_outfit/<int:outfit_id>/', views.assoc_outfit, name='assoc_outfit'),
    path('sonnyangels/<int:sonnyangel_id>/unassoc_outfit/<int:outfit_id>/', views.unassoc_outfit, name='unassoc_outfit'),
    path('outfits/', views.OutfitList.as_view(), name='outfits_index'),
    path('outfits/<int:pk>/', views.OutfitDetail.as_view(), name='outfits_detail'),
    path('outfits/create/', views.OutfitCreate.as_view(), name='outfits_create'),
    path('outfits/<int:pk>/update/', views.OutfitUpdate.as_view(), name='outfits_update'),
    path('outfits/<int:pk>/delete/', views.OutfitDelete.as_view(), name='outfits_delete'),   
]