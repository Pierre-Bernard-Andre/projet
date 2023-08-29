import os
import re
import argparse

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        return "Le fichier spécifié n'a pas été trouvé."

def afficher_texte(texte):
    print("Contenu du fichier :\n")
    print(texte)

def mettre_a_jour_texte(texte):
    print("\nÉdition du texte : (Appuyez sur Ctrl+D pour terminer l'édition)")
    nouvelle_version = []
    while True:
        try:
            ligne = input()
        except EOFError:
            break
        nouvelle_version.append(ligne)
    return '\n'.join(nouvelle_version)

def nettoyer_texte(texte):
    texte_nettoye = ' '.join(texte.split())  # Supprime les espaces blancs inutiles.
    return texte_nettoye

def rechercher_et_remplacer(texte, recherche, remplacement):
    texte_modifie = re.sub(recherche, remplacement, texte)
    return texte_modifie

def enregistrer_texte(nom_fichier, texte):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte)
    print("Le texte a été enregistré dans le fichier avec succès.")

def ligne_de_commande():
    parser = argparse.ArgumentParser(description="Éditeur de texte Python (Interface en ligne de commande)")
    parser.add_argument("fichier", help="Nom du fichier texte")
    parser.add_argument("--nettoyer", action="store_true", help="Nettoyer le texte")
    parser.add_argument("--rechercher", help="Mot ou motif à rechercher")
    parser.add_argument("--remplacer", help="Remplacement pour la recherche")

    args = parser.parse_args()

    nom_fichier = args.fichier
    texte = lire_fichier(nom_fichier)

    if texte:
        if args.nettoyer:
            texte = nettoyer_texte(texte)

        if args.rechercher and args.remplacer:
            texte = rechercher_et_remplacer(texte, args.rechercher, args.remplacer)

        afficher_texte(texte)

        texte = mettre_a_jour_texte(texte)
        enregistrer_texte(nom_fichier, texte)

def menu_principal():
    print("Éditeur de texte Python (Menu Principal)\n")
    nom_fichier = input("Entrez le nom du fichier texte : ")

    texte = lire_fichier(nom_fichier)

    if texte:
        afficher_texte(texte)

        while True:
            print("\nOptions :")
            print("1. Mettre à jour le texte")
            print("2. Nettoyer le texte")
            print("3. Rechercher et remplacer")
            print("4. Enregistrer")
            print("5. Enregistrer dans un nouveau fichier")
            print("6. Quitter sans enregistrer")
            print("7. Utiliser l'interface en ligne de commande")
            choix = input("Choisissez une option (1/2/3/4/5/6/7) : ")

            if choix == '1':
                texte = mettre_a_jour_texte(texte)
                afficher_texte(texte)
            elif choix == '2':
                texte = nettoyer_texte(texte)
                afficher_texte(texte)
            elif choix == '3':
                recherche = input("Mot ou motif à rechercher : ")
                remplacement = input("Remplacement : ")
                texte = rechercher_et_remplacer(texte, recherche, remplacement)
                afficher_texte(texte)
            elif choix == '4':
                enregistrer_texte(nom_fichier, texte)
            elif choix == '5':
                enregistrer_texte(nom_fichier, texte, nouveau_fichier=True)
            elif choix == '6':
                break
            elif choix == '7':
                ligne_de_commande()
                break
            else:
                print("Option invalide. Veuillez choisir 1, 2, 3, 4, 5, 6 ou 7.")

if __name__ == "__main__":
    menu_principal()
