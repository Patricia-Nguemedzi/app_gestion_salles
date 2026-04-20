from data.dao_salle import DataSalle
from models.salle import Salle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.codes or not salle.descriptions or not salle.categorie:
            return False, "Erreur : Toutes les informations sont obligatoires."

        if salle.capacite < 1:
            return False, "Erreur : La capacité doit être d'au moins 1 personne."

        self.dao_salle.insert_salle(salle)
        return True, f"La salle {salle.codes} a été ajoutée avec succès."