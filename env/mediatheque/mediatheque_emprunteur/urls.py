from django.urls import path
from mediatheque_admin import views as admin_views

urlpatterns = [
    path('', admin_views.membre, name='home_membre'),
]