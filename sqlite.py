# Importation des modules nécessaires
import sqlite3, re,os
# Lecture du contenu du fichier HTML généré par Unitex
html = open("corpus-medical_snt/concord.html",'r',encoding="utf-8").read()
# Utilisation d'une expression régulière pour extraire les données pertinentes du fichier HTML
data = re.findall(r'<a href=\"[0-9 ]+\">(.+)</a>',html)
# Suppression de la base de données SQLite s'il existe déjà
if os.path.exists("extraction.db"):
    os.remove("extraction.db")
# Connexion à la base de données SQLite
database= sqlite3.connect("extraction.db")
# Création de la table "extraction" avec les colonnes "id" et "posologie"
database.execute("CREATE TABLE extraction(id INT PRIMARY KEY NOT NULL , posologie TEXT NOT NULL)")
# Insertion des données extraites dans la table "extraction"
for i in range(len(data)):
    database.execute("INSERT INTO extraction VALUES (?,?)",(i+1,data[i]))
 # Validation des modifications dans la base de données
database.commit()
# Fermeture de la connexion à la base de données  
database.close() #/facultatif