import urllib.request
import re
import string
import sys
# Fonction pour récupérer les arguments en ligne de commande
def get_argvs():
    if len(sys.argv) != 3 : #verifier s'il y a le nombre correct des arguments
        print("nombre des arguments est invalide")
        exit()
    else:
        if (not re.match("([A-Z]|[a-z])(-)([A-Z]|[a-z])",sys.argv[1]) or (sys.argv[1][0].upper()>sys.argv[1][2].upper())):
            #verfier si le format du premier arguments est valide
            print("Format de l'interval n'est pas valide")
            exit()
        if (not sys.argv[2].isdigit()):
            #verfier si le format du 2éme arguments est valide
            print("Format du port n'est pas valide")
            exit()

    return sys.argv[1][0].upper(),sys.argv[1][2].upper(),sys.argv[2]
# Fonction pour récupérer les médicaments en fonction de l'intervalle et du port spécifiés
def fetch_meds(first_char,second_char,port):
    alphabet_list = string.ascii_uppercase #list des alphabets en majescule
    list_of_meds = []
    for i in range(alphabet_list.index(first_char),alphabet_list.index(second_char)+1):
        url = urllib.request.urlopen("http://127.0.0.1:"+port+"/vidal/vidal-Sommaires-Substances-"+ alphabet_list[i] +".html")
        list_of_meds.extend(fetch_page(url,alphabet_list[i]))
    return list_of_meds
# Fonction pour extraire les noms de médicaments à partir d'une page HTML
def fetch_page(url,lettre):
    file_text = url.read().decode("utf-8")

    print("Recherche dans le fichier de la lettre : "+lettre)

    occurences = re.findall("(<a href=\"Substance/.+.htm\">)(.+?)(</a>)",file_text)

    info[lettre] = len(occurences)#le dictionnaire des statistique pour le fichier info1.txt
    return [occurences[i][1] for i in range(len(occurences))]
# Fonction pour générer le fichier "subst.dic"
def generate_dictionary(list_of_meds):
    dictionnaire = open('subst.dic','w',encoding="utf-16le")
    dictionnaire.write("\ufeff")

    for i in list_of_meds:
        dictionnaire.write(i+",.N+subst\n")

    dictionnaire.close()
    return
# Fonction pour générer le fichier "infos1.txt"
def generate_stats(info):
    stats = open("infos1.txt","w")

    total = 0
    for i in info:
        stats.write(i+" : "+str(info[i])+"\n")
        total += info[i]

    stats.write("Total : "+str(total))
    stats.close()
    return

if __name__ == "__main__":
    info = {} #le dictionnaire des statistiques

    first_char,second_char,port=get_argvs()#recupérer les information des arguments

    list_of_meds = fetch_meds(first_char,second_char,port)#recupérer la liste des médicaments de la page du serveur 

    generate_dictionary(list_of_meds) #générer le fichier subt.dic

    generate_stats(info) #générer le fichier info1.txt