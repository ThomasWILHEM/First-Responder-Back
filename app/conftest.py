import pytest
import mysql.connector

@pytest.fixture(scope="session")
def initialize_database():
    database_config = {
        'host': 'localhost',
        'port': 3307,
        'user': 'operator',
        'password': 'admin',
        'database': 'first-responder-tests',
    }

    try:
        # Établir une connexion à la base de données MariaDB
        conn = mysql.connector.connect(**database_config)

        # Créer un objet curseur pour exécuter des commandes SQL
        cursor = conn.cursor()

        try:
            # Désactiver les contraintes de clé étrangère
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Lire le script SQL depuis le fichier
            with open("app/utils/create_tests_base.sql", "r") as sql_file:
                sql_script = sql_file.read()

            # Exécuter le script SQL
            cursor.execute(sql_script)

            # Valider les modifications dans la base de données
            conn.commit()

        except Exception as e:
            print(f"Erreur lors de l'exécution du script SQL : {e}")

        finally:
            # Réactiver les contraintes de clé étrangère
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

            # Fermer le curseur
            cursor.close()

    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
