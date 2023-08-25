class Véhicule:
    def __init__(self, marque, modèle, année, tarif_journalier):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.tarif_journalier = tarif_journalier

    def afficher_info(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modèle}")
        print(f"Année : {self.année}")
        print(f"Tarif de Location Journalier : {self.tarif_journalier:.2f} $")

class Voiture(Véhicule):
    def __init__(self, marque, modèle, année, tarif_journalier, nombre_de_places):
        super().__init__(marque, modèle, année, tarif_journalier)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        print(f"Nombre de Places : {self.nombre_de_places}")

class Moto(Véhicule):
    def __init__(self, marque, modèle, année, tarif_journalier, type_moteur):
        super().__init__(marque, modèle, année, tarif_journalier)
        self.type_moteur = type_moteur

    def afficher_info(self):
        super().afficher_info()
        print(f"Type de Moteur : {self.type_moteur}")

class Vélo(Véhicule):
    def __init__(self, marque, modèle, année, tarif_journalier, type_cadre):
        super().__init__(marque, modèle, année, tarif_journalier)
        self.type_cadre = type_cadre

    def afficher_info(self):
        super().afficher_info()
        print(f"Type de Cadre : {self.type_cadre}")

class Location:
    def __init__(self, véhicule, jours_location):
        self.véhicule = véhicule
        self.jours_location = jours_location

    def calculer_coût_total(self):
        return self.véhicule.tarif_journalier * self.jours_location

    def afficher_reçu(self):
        print("Reçu de Location")
        print("-----------------")
        self.véhicule.afficher_info()
        print(f"Jours de Location : {self.jours_location}")
        coût_total = self.calculer_coût_total()
        print(f"Coût Total : {coût_total:.2f} $")

# Code pour tester le système

voiture = Voiture("Toyota", "Camry", 2023, 50.0, 5)
moto = Moto("Harley-Davidson", "Sportster", 2023, 75.0, "V-twin")
vélo = Vélo("Trek", "VTT", 2023, 15.0, "Montagne")

location1 = Location(voiture, 3)
location2 = Location(moto, 5)
location3 = Location(vélo, 2)

location1.afficher_reçu()
print()
location2.afficher_reçu()
print()
location3.afficher_reçu()
