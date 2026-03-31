dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', 'h':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'o':'و', 'u':'و', 'i':'ي', 'y':'ي', '2': 'ء'
                 }

def conv_lett(mot):
    last_CV = False # "est-ce qu'on vient de voir une voyelle ?"
                    # aucune voyelle en vue au début du mot donc False
                    # NB : EN ARABE DEUX VOYELLES NE PEUVENT SE SUIVRE
                    # Si on repère une voyelle avant puis après, on ignore la deuxième
    voyelles = ['a', 'i', 'y', 'o', 'ou', 'e']
    mot_arabe = []
    i = 0

    while i < len(mot):
        if mot[i:i+2] in dico_arabizi: # digrammes
            mot_arabe.append(dico_arabizi[mot[i:i+2]])
            i += 2
        elif i+1 < len(mot) and mot[i] == mot[i+1]: # mot[i] == mot[i+1] consonne géminée 
            # i+1 < len(mot) pour éviter les crash en fin de mots si i+1 > len(mot)
            mot_arabe.append(dico_arabizi[mot[i]])
            last_CV = False
            mot_arabe.append('ّ')
            i += 2
        elif mot[i] in voyelles: # voyelle repérée 
            if last_CV: # est-ce qu'on en a vu une ? 
                i += 1 # si oui, on l'ignore et on passe au caractère suivant 
            else:
               if mot[i] in dico_arabizi: # la voyelle est dans le dico ? 
                   mot_arabe.append(dico_arabizi[mot[i]]) # --> oui on la transcriit 
               last_CV = True # True, il y a une voyelle 
               i += 1 # alors on passe caractère suivant
        elif mot[i] in dico_arabizi: # consonne
            mot_arabe.append(dico_arabizi[mot[i]])
            last_CV = False
            i += 1
        else: # caractères non reconnus (ponctuation, espaces etc.)
            mot_arabe.append(mot[i])
            i += 1 
    return ''.join(mot_arabe)

if __name__ == "__main__":
      mot = (input("Entrez un mot : ")).lower()
      print(conv_lett(mot))

