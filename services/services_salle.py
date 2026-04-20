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

    def modifier_salle(self, salle):
        if not salle.codes or salle.capacite < 1:
            return False, "Données invalides pour la modification."

        self.dao_salle.update_salle(salle)
        return True, "Modification réussie."

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return True, "Suppression réussie."