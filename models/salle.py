class Salle:
    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print("-" * 50)
        print(f"Details complets de la salle de classe {self.code}")
        print("-" * 50)
        print(f"code        : {self.code}")
        print(f"description : {self.description}")
        print(f"categorie   : {self.categorie}")
        print(f"capacite    : {self.capacite} personnes.")
        print("-" * 50)



