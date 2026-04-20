from models.salle import Salle
from data.dao_salle import DataSalle

'''def test_dao():
    dao = DataSalle()

    print("premier test:  connexion à la base de données ")
    connexion = dao.get_connection()

    if connexion:
        print("connexion à la base de donnée reussie avec succès")
        connexion.close()
    else:
        print("echec de la connexion à la bae de donnée")

        return test_dao()'''



'''def test_dao():
    dao = DataSalle()
    print("deuxième test: Ajout d'une salle à la base de donnée.")
    ma_salle = Salle("C250", "lab informatique", "programmation", 35)
    ta_salle=Salle("B430", "salle d'activité", "Auditorium", 500)
    dao.insert_salle(ma_salle)
    dao.insert_salle(ta_salle)'''



'''def test_dao():
    dao = DataSalle()
    print("troisième test: supression d'une salle à la base de donnée")
    dao.delete_salle("B430")'''

def test_modification():
    dao = DataSalle()

    print("quatrième test: Modification d'une salle  à la base de donnée")
    salle_a_modifier= Salle("C250", "lab réseautique", "Network", 43)
    dao.update_salle(salle_a_modifier)
    '''salle_verifiee = dao.get_salle("C250")
    print(f"Vérification des nouvelles données : {salle_verifiee}")'''


if __name__ == "__main__":
    test_modification()






