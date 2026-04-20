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

def test_dao():
    dao = DataSalle()
    print("deuxième test: Ajout d'une salle à la base de donnée.")
    S1 = Salle("C250", "lab informatique", "programmation", 35)
    S2 = Salle("B430", "salle d'activité", "Auditorium", 500)
    S3 = Salle("B201", "Salle de classe standard", "Amphithéâtre", 1000)
    S4 = Salle("C102", "Salle de conférence", "Réunion", 12)
    S5 = Salle("AM01", "salle des langues", "Anglais/Français", 260)

    dao.insert_salle(S1)
    dao.insert_salle(S2)
    dao.insert_salle(S3)
    dao.insert_salle(S4)
    dao.insert_salle(S5)

if __name__ == "__main__":
    test_dao()

'''def test_dao():
    dao = DataSalle()
    print("troisième test: supression d'une salle à la base de donnée")
    dao.delete_salle("B430")

def test_modification():
    dao = DataSalle()

    print("quatrième test: Modification d'une salle  à la base de donnée")
    salle_a_modifier= Salle("C250", "lab réseautique", "Network", 43)
    dao.update_salle(salle_a_modifier)

def test_recherche():
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
        print(f"Aucune salle ne porte le code : {code_cherche}")


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

from models.salle import Salle
from services.services_salle import ServiceSalle


def test_service():
    service = ServiceSalle()

    print("Test Service : Ajouter une salle invalide (Capacité 0)")
    salle_nulle = Salle("TEST", "Nulle", "Inconnu", 0)
    succes, message = service.ajouter_salle(salle_nulle)

    if not succes:
        print(f"Résultat attendu : {message}")

def test_service():
    service = ServiceSalle()
    print("\n Test Service : Récupérer toutes les salles")
    liste = service.recuperer_salles()
    for s in liste:
        print(f"Salle trouvée : {s.codes}")

if __name__ == "__main__":
    test_service()


from views.view_salle import ViewSalle

if __name__ == "__main__":
    app = ViewSalle()
    app.mainloop()'''



