from django.db import models


# Create your models here.

class Emprunteur(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_creation = models.DateField(auto_now_add=True)
    bloque = models.BooleanField(default=False)

    def statut_emprunteur(self):
        if self.bloque == 1:
            return 'red'
        else:
            return 'green'
    def __str__(self):
        return self.first_name+' '+self.last_name

class Media(models.Model):
    type_media = models.TextChoices("type_media", "DVD CD LIVRE")
    media_name  = models.CharField(max_length=100)
    media = models.CharField(choices=type_media, max_length=10)
    date_emprunt= models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(Emprunteur, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Livre(Media):
    livre_auteur = models.CharField(max_length=100)


class Cd(Media):
    cd_artiste = models.CharField(max_length=100)


class Dvd(Media):
    dvd_realisateur = models.CharField(max_length=100)


class Jeu_plateau(models.Model):
    jeu_name = models.CharField(max_length=100)
    jeu_createur  = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(Emprunteur, null=True, blank=True, on_delete=models.CASCADE)

# Create your models here.
