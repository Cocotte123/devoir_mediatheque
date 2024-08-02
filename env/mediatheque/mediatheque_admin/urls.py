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
    path('retour_jeuplateau/<int:id>/', views.retour_jeuplateau, name='retour_jeuplateau'),
    path('emprunt_livre_page/', views.emprunt_livre_page, name='emprunt_livre_page'),
    path('emprunt_livre/', views.emprunt_livre, name='emprunt_livre'),
    path('emprunt_cd_page/', views.emprunt_cd_page, name='emprunt_cd_page'),
    path('emprunt_cd/', views.emprunt_cd, name='emprunt_cd'),
    path('emprunt_dvd_page/', views.emprunt_dvd_page, name='emprunt_dvd_page'),
    path('emprunt_dvd/', views.emprunt_dvd, name='emprunt_dvd'),
    path('retour_livre_page/', views.retour_livre_page, name='retour_livre_page'),
    path('retour_livre/', views.retour_livre, name='retour_livre'),
    path('retour_cd_page/', views.retour_cd_page, name='retour_cd_page'),
    path('retour_cd/', views.retour_cd, name='retour_cd'),
    path('retour_dvd_page/', views.retour_dvd_page, name='retour_dvd_page'),
    path('retour_dvd/', views.retour_dvd, name='retour_dvd'),
]


