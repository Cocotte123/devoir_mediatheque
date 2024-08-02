from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .views import *

# Create your tests here.
class TestCaseProject(TestCase):
    def setUp(self):

        self.client = Client()

        self.emprunteur_data = {
            'first_name': 'Tony',
            'last_name': 'Stark',
        }


    def test_add_emprunteur(self):

        url = reverse('add_emprunteur')

        response = self.client.post(url, data=self.emprunteur_data)

        self.assertTrue(Emprunteur.objects.filter(first_name='Tony').exists())


    def test_delete_emprunteur(self):

        self.emprunteur_data = {
            'first_name': 'Tony',
            'last_name': 'Stark',
        }

        self.emprunteur = Emprunteur.objects.create(**self.emprunteur_data)

        url = reverse('delete_emprunteur', args='1')

        response = self.client.post(url)

        self.assertFalse(Emprunteur.objects.filter(first_name='Tony').exists())

    def test_update_emprunteur(self):

        self.emprunteur_data = {
            'first_name': 'Tony',
            'last_name': 'Stark',
        }

        self.emprunteur = Emprunteur.objects.create(**self.emprunteur_data)

        url = reverse('update_emprunteur', args='1')

        response = self.client.post(url)

        updated = Emprunteur.objects.get(first_name='Tony')
        self.assertTrue(updated.bloque)


    def test_emprunt_jeuplateau_page(self):

        self.jeuplateau_data = {
            'jeu_name': 'puissance4',
            'jeu_createur': 'inconnu'
        }

        self.jeuplateau = Jeu_plateau.objects.create(**self.jeuplateau_data)

        url = reverse('emprunt_jeuplateau_page', args='1')

        response = self.client.get(url)

        self.assertTemplateUsed(response,'emprunt_jeuplateau.html')


    def test_emprunt_jeuplateau(self):
        self.jeuplateau_data = {
            'jeu_name': 'puissance4',
            'jeu_createur': 'inconnu'
        }

        self.jeuplateau = Jeu_plateau.objects.create(**self.jeuplateau_data)

        self.emprunteur = {
            'first_name': 'Tony',
            'last_name': 'Stark',
        }

        self.emprunteur = Emprunteur.objects.create(**self.emprunteur_data)

        url = reverse('emprunt_jeuplateau', args='1')

        response = self.client.post(url, {'emprunteur':'1', 'date_emprunt': '2024-08-01'})

        updated = Jeu_plateau.objects.get(jeu_name='puissance4')
        self.assertFalse(updated.disponible)
        self.assertIsNotNone(updated.emprunteur)
        self.assertIsNotNone(updated.date_emprunt)

    def test_retour_jeuplateau(self):
        self.jeuplateau_data = {
            'jeu_name': 'puissance4',
            'jeu_createur': 'inconnu'
        }

        self.jeuplateau = Jeu_plateau.objects.create(**self.jeuplateau_data)

        url = reverse('retour_jeuplateau', args='1')

        response = self.client.post(url)

        updated = Jeu_plateau.objects.get(jeu_name='puissance4')
        self.assertTrue(updated.disponible)
        self.assertIsNone(updated.emprunteur)
        self.assertIsNone(updated.date_emprunt)

    def test_add_media(self):
        self.media_data = {
            'media_name': 'Le petit Prince',
            'media': 'LIVRE',
            'auteur': 'Saint Exupéry'
        }

        url = reverse('add_media')

        response = self.client.post(url, data=self.media_data)

        self.assertTrue(Livre.objects.filter(media_name= 'Le petit Prince').exists())
        self.assertFalse(Cd.objects.filter(media_name='Le petit Prince').exists())
        self.assertFalse(Dvd.objects.filter(media_name='Le petit Prince').exists())