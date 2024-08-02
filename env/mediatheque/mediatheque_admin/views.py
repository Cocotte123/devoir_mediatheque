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
    datas_emprunteur = Emprunteur.objects.all().filter(bloque = "False")
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


def retour_jeuplateau(request,id):
    if request.method == 'POST':
       pi = Jeu_plateau.objects.get(pk=id)
       pi.disponible = True
       pi.date_emprunt = None
       pi.emprunteur = None
       pi.save()
       return HttpResponseRedirect('/')


def emprunt_livre_page(request):
    datas_emprunteur = Emprunteur.objects.all().filter(bloque = "False")
    datas_livre = Livre.objects.all().filter(disponible = "True")

    context = {
        'datas_emprunteur': datas_emprunteur,
        'datas_livre': datas_livre
    }


    return render(request, 'emprunt_livre.html', context)


def emprunt_livre(request):
    if request.method == 'POST':
       pi = Livre.objects.get(pk=request.POST['livre'])
       pi.disponible = False
       pi.date_emprunt = request.POST['date_emprunt']
       pi.emprunteur = Emprunteur.objects.get(pk=request.POST['emprunteur'])
       pi.save()
       return HttpResponseRedirect('/')


def emprunt_cd_page(request):
    datas_emprunteur = Emprunteur.objects.all().filter(bloque = "False")
    datas_cd = Cd.objects.all().filter(disponible = "True")

    context = {
        'datas_emprunteur': datas_emprunteur,
        'datas_cd': datas_cd
    }


    return render(request, 'emprunt_cd.html', context)


def emprunt_cd(request):
    if request.method == 'POST':
       pi = Cd.objects.get(pk=request.POST['cd'])
       pi.disponible = False
       pi.date_emprunt = request.POST['date_emprunt']
       pi.emprunteur = Emprunteur.objects.get(pk=request.POST['emprunteur'])
       pi.save()
       return HttpResponseRedirect('/')


def emprunt_dvd_page(request):
    datas_emprunteur = Emprunteur.objects.all().filter(bloque = "False")
    datas_dvd = Dvd.objects.all().filter(disponible = "True")

    context = {
        'datas_emprunteur': datas_emprunteur,
        'datas_dvd': datas_dvd
    }


    return render(request, 'emprunt_dvd.html', context)


def emprunt_dvd(request):
    if request.method == 'POST':
       pi = Dvd.objects.get(pk=request.POST['dvd'])
       pi.disponible = False
       pi.date_emprunt = request.POST['date_emprunt']
       pi.emprunteur = Emprunteur.objects.get(pk=request.POST['emprunteur'])
       pi.save()
       return HttpResponseRedirect('/')


def retour_livre_page(request):
    datas_livre = Livre.objects.all().filter(disponible = "False")

    context = {
        'datas_livre': datas_livre
    }


    return render(request, 'retour_livre.html', context)


def retour_livre(request):
    if request.method == 'POST':
       pi = Livre.objects.get(pk=request.POST['livre'])
       pi.disponible = True
       pi.date_emprunt = None
       pi.emprunteur = None
       pi.save()
       return HttpResponseRedirect('/')


def retour_cd_page(request):
    datas_cd = Cd.objects.all().filter(disponible = "False")

    context = {
        'datas_cd': datas_cd
    }


    return render(request, 'retour_cd.html', context)


def retour_cd(request):
    if request.method == 'POST':
       pi = Cd.objects.get(pk=request.POST['cd'])
       pi.disponible = True
       pi.date_emprunt = None
       pi.emprunteur = None
       pi.save()
       return HttpResponseRedirect('/')


def retour_dvd_page(request):
    datas_dvd = Dvd.objects.all().filter(disponible = "False")

    context = {
        'datas_dvd': datas_dvd
    }


    return render(request, 'retour_dvd.html', context)


def retour_dvd(request):
    if request.method == 'POST':
       pi = Dvd.objects.get(pk=request.POST['dvd'])
       pi.disponible = True
       pi.date_emprunt = None
       pi.emprunteur = None
       pi.save()
       return HttpResponseRedirect('/')


def membre(request):
    livre = Livre.objects.all().filter(disponible = "True")
    cd = Cd.objects.all().filter(disponible = "True")
    dvd = Dvd.objects.all().filter(disponible = "True")
    datas_media = livre.union(cd,dvd)
    datas_jeuplateau = Jeu_plateau.objects.all().filter(disponible = "True")

    context = {

        'datas_media': datas_media,
        'datas_jeuplateau': datas_jeuplateau,
    }


    return render(request, 'home_membre.html', context)