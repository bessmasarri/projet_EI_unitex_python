import re, sys
from string import ascii_uppercase

# Fonction pour extraire les noms de médicaments du corpus médical
def fetch_corpus():
    corpus_content = open(sys.argv[1], 'r', encoding='utf-8').readlines()
    enrich_list = []
    for i in corpus_content:
# Utilisation d'une expression régulière pour extraire les noms de médicaments
        x = re.findall( r"[^[A-Z]?\s?([A-Z]{4,})(\s\d+)?\s(:\s\d+\s\w|\d+,?\d?\s(mg|ml|µg|mcg|g|cp|amp|flacon))", i,re.I)

        if x and x[0][0] != "intraveineuse":
            enrich_list.append(x[0][0].lower()) # Ajout en minuscules à la liste
    return enrich_list

# Fonction pour générer le fichier "subst_corpus.dic" à partir de la liste enrich_list
def generate_subst_corpus_dic():
    subst_corpus = open("subst_corpus.dic","w",encoding = "utf-16le")
    subst_corpus.write("\ufeff") # BOM (Byte Order Mark) pour UTF-16 LE
    for i in list_of_enrich:
        subst_corpus.write(i + ",.N+subst\n")
    return

# Fonction pour trier et éliminer les doublons dans le fichier "subst.dic"
def generate_subst_dic():
	organized_list = list(set(list_of_enrich)) # Supprime les doublons
	organized_list.sort() # Trie la liste
	print(organized_list)
	for i in range(len(organized_list)) :
		organized_list[i] += ",.N+subst\n"
	#print(organized_list,len(organized_list))
	old_dic = open("subst.dic","r",encoding="utf-16le").readlines()
	old_dic.extend(organized_list)
# Supprime les doublons du dictionnaire existant
	clean_old_dic = list(set(old_dic))
	clean_old_dic.sort() # Trie la liste des doublons supprimés
	print(len(clean_old_dic))
	new_dic = open("subst.dic","w",encoding="utf-16le")
	for i in old_dic:
		new_dic.write(i)
	return
	
# Fonction pour générer les statistiques des fichiers "infos2.txt" et "infos3.txt"
def generate_stats_corpus():
	stats=open("infos2.txt","w")
	med=open("infos1.txt","r").readlines()
	final=open("infos3.txt","w")
	list_enr=open("subst_corpus.dic","r",encoding='utf-16le').readlines()
	for lettre,i in zip(ascii_uppercase,med):
		x=re.findall(r"(\d+$)",i,re.I)
		nbr_entite=0
		for let in list(set(list_enr)):
			if lettre == let[0].upper() :
				nbr_entite += 1
		stats.write("Nombre d'entité médicale commençant par "+lettre+" = "+str(nbr_entite)+"\n")
		final.write("Nombre d'entité médicale commençant par "+lettre+" = "+str(nbr_entite+int(x[0]))+"\n")
	stats.write("Nombre total d'entités médicales de type noms de médicaments par gamme = " +str(len(list(set(list_enr)))))
	for j in med:
		x=re.findall(r"(\d+$)",j,re.I)
	final.write("Nombre total d'entités médicales  = " +str(len(list(set(list_enr)))+int(x[0])))
	
	final.close()
	stats.close()
	return

	

if __name__ == "__main__":
	info2={}
	list_of_enrich = fetch_corpus()
	generate_subst_corpus_dic()
	generate_subst_dic()
	generate_stats_corpus()