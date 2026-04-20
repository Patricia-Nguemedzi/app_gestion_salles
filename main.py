from models.salle import Salle
from data.dao_salle import DataSalle

def test_dao():
    dao = DataSalle()

    print("premier test:  connexion à la base de données ")
    connexion = dao.get_connection()

    if connexion:
        print("connexion à la base de donnée reussie avec succès")
        connexion.close()
    else:
        print("echec de la connexion à la bae de donnée")

        return

'''def test_dao():
    dao = DataSalle()
    print("deuxième test: Ajout d'une salle à la base de donnée.")
    ma_salle = Salle("C250", "lab informatique", "programmation", 35)
    ta_salle=Salle("B430", "salle d'activité", "Auditorium", 500)
    dao.insert_salle(ma_salle)
    dao.insert_salle(ta_salle)'''

if __name__ == "__main__":
    test_dao()






