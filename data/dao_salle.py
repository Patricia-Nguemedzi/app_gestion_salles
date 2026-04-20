import mysql.connector
import json

class DataSalle:
    def get_connection(self):

        try:
            with open ("data/config.json", "r", encoding="Utf-8") as f:
                config = json.load(f)

            connection = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
            return connection
        except mysql.connector.Error as error:
            print(f"erreur de connexion : {error}")
            return None

    def insert_salle(self, salle):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                "INSERT INTO salle (codes, descriptions,categorie, capacite) values (%s, %s, %s, %s)",
                (salle.codes, salle.descriptions, salle.categorie, salle.capacite)
                )

                connection.commit()
                print(f"La salle {salle.codes} a été ajoutée avec succès.")

            except mysql.connector.Error as err:
                print(f"Erreur lors de l'insertion : {err}")

            finally:
                cursor.close()
                connection.close()

    def update_salle(self, salle):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "UPDATE salle SET descriptions = %s, categorie = %s, capacite = %s where codes = %s",
                    (salle.descriptions, salle.categorie, salle.capacite, salle.codes)
                )
                connection.commit()
                print(f"la salle {salle.codes} a été mis à jour avec succès ")
            except mysql.connector.Error as err:
                print(f"Erreur lors de la mise à jour de la salle : {err}")
            finally:
                cursor.close()
                connection.close()

    def delete_salle(self, codes):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "DELETE FROM salle WHERE codes = %s", (codes,)
                )
                connection.commit()
                print(f"la salle avec le code : {codes} a été supprimé.")

            except mysql.connector.Error as err:
                print(f"Erreur lors de la suppression : {err}")
            finally:
                cursor.close()
                connection.close()


    def get_salle(self, codes):
        connection = self.get_connection()
        salle = None
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    "SELECT * FROM salle WHERE codes = %s", (codes,)
                )
                salle = cursor.fetchone()
                while cursor.nextset():
                    pass
            except mysql.connector.Error as err:
                print(f"Erreur lors de la recherche : {err}")
            finally:
                cursor.close()
                connection.close()

            return salle

    def get_salles(self):
        connection = self.get_connection()
        liste_salle = []
        if connection:
            try:
                cursor = connection.cursor(dictionary=True, buffered=True)
                cursor.execute("SELECT * FROM salle")
                liste_salle = cursor.fetchall()
            except mysql.connector.Error as err:
                print(f"Erreur lors de la récupération : {err}")
            finally:
                cursor.close()
                connection.close()

        return liste_salle












