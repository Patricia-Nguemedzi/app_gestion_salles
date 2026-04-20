class Salle:
    def __init__(self, codes, descriptions, categorie, capacite):
        self.codes = codes
        self.descriptions = descriptions
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print("-" * 50)
        print(f"Details complets de la salle de classe {self.codes}")
        print("-" * 50)
        print(f"code        : {self.codes}")
        print(f"description : {self.descriptions}")
        print(f"categorie   : {self.categorie}")
        print(f"capacite    : {self.capacite} personnes.")
        print("-" * 50)



