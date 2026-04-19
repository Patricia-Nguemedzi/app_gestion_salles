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
                "INSERT INTO salle (code, description,categorie, capacite) values (%s, %s, %s, %s)",
                (salle.code, salle.description, salle.categorie, salle.capacite)
                )

                connection.commit()
                print(f"La salle {salle.code} a été ajoutée avec succès.")

            except mysql.connector.Error as err:
                print(f"Erreur lors de l'insertion : {err}")

            finally:
                cursor.close()
                connection.close()




