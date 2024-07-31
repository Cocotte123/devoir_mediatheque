from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_emprunteur/', views.add_emprunteur, name='add_emprunteur'),
    path('delete_emprunteur/<int:id>/', views.delete_emprunteur, name='delete_emprunteur'),
    path('update_emprunteur/<int:id>/', views.update_emprunteur, name='update_emprunteur'),
    path('add_media/', views.add_media, name='add_media'),
    path('add_jeuplateau/', views.add_jeuplateau, name='add_jeuplateau'),
    path('emprunt_jeuplateau_page/<int:pk>/', views.emprunt_jeuplateau_page, name='emprunt_jeuplateau_page'),
    path('emprunt_jeuplateau/<int:id>/', views.emprunt_jeuplateau, name='emprunt_jeuplateau'),
]


