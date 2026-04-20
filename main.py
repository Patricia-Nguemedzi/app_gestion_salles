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

'''def test_modification():
    dao = DataSalle()

    print("quatrième test: Modification d'une salle  à la base de donnée")
    salle_a_modifier= Salle("C250", "lab réseautique", "Network", 43)
    dao.update_salle(salle_a_modifier)'''

'''def test_recherche():
    dao = DataSalle()
    print("cinquième test: recherche d'une classe par son code")
    code_cherche="C250"
    resultat=dao.get_salle(code_cherche)

    if resultat:
        print(f"Salle trouvée en base de données :")
        print(f"Code : {resultat['codes']}")
        print(f"Description : {resultat['descriptions']}")
        print(f"Capacité : {resultat['capacite']}")
    else:
        print(f"Aucune salle ne porte le code : {code_cherche}")'''


def test_afficher_tout():
    dao = DataSalle()

    print("Sixième test : Récupération de toutes les salles")

    toutes_les_salles = dao.get_salles()

    if toutes_les_salles:
        print(f"{len(toutes_les_salles)} salle(s) trouvée(s) dans la base :\n")

        for salle in toutes_les_salles:
            print(f"Code: {salle['codes']}, Description: {salle['descriptions']}, "
                  f"Catégorie: {salle['categorie']}, Capacité: {salle['capacite']}")
    else:
        print("Empty: La base de données est vide.")


if __name__ == "__main__":
    test_afficher_tout()








