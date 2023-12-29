import os
from os import path
# Vérifier si le dossier corpus-medical_snt existe, le cas échéant, le supprimer
if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")
# Créer le dossier corpus-medical_snt
os.mkdir("corpus-medical_snt")
# Étape 1 : Normalisation du texte
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
# Étape 2 : Tokenisation du texte
# Utilisation du fichier Alphabet.txt pour définir les règles de segmentation
# Exemple : Tokeniser le texte en utilisant les règles définies dans le fichier Alphabet.txt
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
# Étape 3 : Compression du dictionnaire
os.system("UnitexToolLogger Compress subst.dic")
# Étape 4 : Création du dictionnaire et des fichiers Dela_fr.bin
# Utilisation du fichier Alphabet.txt pour la création du dictionnaire
# Exemple : Créer le dictionnaire en respectant les règles définies dans le fichier Alphabet.txt
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin Dela_fr.bin")
# Étape 5 : Conversion du graphe en format FST2
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
# Étape 6 : Recherche des occurrences du graphe dans le texte
# Utilisation du fichier Alphabet.txt pour la recherche des occurrences
# Exemple : Rechercher les occurrences en se basant sur les règles définies dans le fichier Alphabet.txt
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
# Étape 7 : Génération du fichier de concordance
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
