from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def home(request):
    datas_emprunteur = Emprunteur.objects.all()
    datas_media = Livre.objects.all().union(Cd.objects.all(),Dvd.objects.all())
    datas_jeuplateau = Jeu_plateau.objects.all()

    context = {
        'datas_emprunteur': datas_emprunteur,
        'datas_media': datas_media,
        'datas_jeuplateau': datas_jeuplateau,
    }


    return render(request, 'home.html', context)


def add_emprunteur(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_emprunteur = Emprunteur(first_name=first_name, last_name=last_name)
        new_emprunteur.save()
        return HttpResponseRedirect('/')


def delete_emprunteur(request, id):
    if request.method == 'POST':
        pi = Emprunteur.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_emprunteur(request, id):
    if request.method == 'POST':
        pi = Emprunteur.objects.get(pk=id)
        if not pi.bloque:
            pi.bloque = True
        else:
            pi.bloque = False
        pi.save()
        return HttpResponseRedirect('/')


def add_media(request):
    if request.method == 'POST':
        media_name = request.POST['media_name']
        media = request.POST['media']
        auteur = request.POST['auteur']
        if media == "LIVRE":
            new_media = Livre(media_name=media_name, media=media, livre_auteur=auteur)
        elif media == "CD":
            new_media = Cd(media_name=media_name, media=media, cd_artiste=auteur)
        else:
            new_media = DVD(media_name=media_name, media=media, dvd_realisateur=auteur)
        new_media.save()
        return HttpResponseRedirect('/')

# Create your views here.
def add_jeuplateau(request):
    if request.method == 'POST':
        jeu_name = request.POST['jeu_name']
        jeu_createur = request.POST['jeu_createur']
        new_jeuplateau = Jeu_plateau(jeu_name=jeu_name, jeu_createur=jeu_createur)
        new_jeuplateau.save()
        return HttpResponseRedirect('/')


def emprunt_jeuplateau_page(request,pk):
    datas_emprunteur = Emprunteur.objects.all()
    jeuplateau_emprunte = Jeu_plateau.objects.get(id=pk)

    context = {
        'datas_emprunteur': datas_emprunteur,
        'jeuplateau_emprunte': jeuplateau_emprunte
    }


    return render(request, 'emprunt_jeuplateau.html', context)

def emprunt_jeuplateau(request,id):
    if request.method == 'POST':
       pi = Jeu_plateau.objects.get(pk=id)
       pi.disponible = False
       pi.date_emprunt = request.POST['date_emprunt']
       pi.emprunteur = Emprunteur.objects.get(pk=request.POST['emprunteur'])
       pi.save()
       return HttpResponseRedirect('/')