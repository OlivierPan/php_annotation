from os import listdir
import os
from os.path import isfile, join
import random
import re
# FAIRE CSV, CORPUS/TITRE DE L'ARTICLE/INDEX DE PHRASE, SQL POUR INTERROGER LE CSV=TRANSFORMATION EN SQL
# 
# 
#onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
#print(onlyfiles)
#print(os.listdir('.'))
def tirerphrasesaleatoire(repertoire):
    f = open(str(repertoire.split('/')[-1])+'_corpus.txt','w+',encoding = "utf-8")
    all_phrases_repertoire = list()
    dico_index = dict()
    
    for file in os.listdir(repertoire):
        if file[0] =='.':continue
        path_to_file = os.path.join(repertoire,file)
        with open(path_to_file,"r",encoding="utf-8") as fichier:
            texte = fichier.read()
            list_phrase = texte.split("\n")
            nb_phrases_txt = len(list_phrase)
        nb_phrases_somme = len(all_phrases_repertoire)    
        all_phrases_repertoire.extend(list_phrase)
        nb_phrases_somme = len(all_phrases_repertoire)
        dico_index[file] = ([nb_phrases_somme,nb_phrases_txt])
        #print(len(all_phrases_repertoire))
    phrases_chosen = random.sample(all_phrases_repertoire,100)    
    try:
        i = 0
        for phrase in phrases_chosen:#!!!!!!!!!!!
            if len(phrase) > 30:#!!!!!!!!!!!!!!
                if i < 22:#!!!!!!!!!!!!!!!
                    i+=1
                    index = all_phrases_repertoire.index(phrase)
                    print(index)# lots of white line
                    f.write(all_phrases_repertoire[index-2]+'\n')
                    f.write(all_phrases_repertoire[index-1]+'\n')
                    f.write(phrase+'\n')
                    f.write(all_phrases_repertoire[index+1]+'\n')
                    f.write(all_phrases_repertoire[index+2]+'\n')
                    f.write('###################################\n')
                else:
                    break
    except:
        print('something wrong!')
    f.close()
    return True

if __name__ == "__main__":
    tirerphrasesaleatoire('./PtitLibeTXT/PtitLibe')
    #tirerphrasesaleatoire('./Murail/Murail_TXT')
    #tirerphrasesaleatoire('./ChienPourriTXT/ChienPourri')              

