dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', 'h':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'o':'و', 'u':'و', 'i':'ي', 'y':'ي', '2': 'ء'
                 }

def conv_lett(mot):
    last_CV = False
    voyelles = ['a', 'i', 'y', 'o', 'ou', 'e']
    mot_arabe = []
    i = 0
    while i < len(mot):
        if mot[i:i+2] in dico_arabizi:
            mot_arabe.append(dico_arabizi[mot[i:i+2]])
            i += 2
        elif mot[i] == mot[i+1]:
            mot_arabe.append(dico_arabizi[mot[i]])
            mot_arabe.append('ّ')
            i += 2
        elif mot[i] in voyelles:
            if last_CV: 
                i += 1
            else:
               if mot[i] in dico_arabizi:
                   mot_arabe.append(dico_arabizi[mot[i]])
               last_CV = True
               i += 1
        elif mot[i] in dico_arabizi:
            mot_arabe.append(dico_arabizi[mot[i]])
            i += 1
        else:
            mot_arabe.append(mot[i])
            i += 1 
    return ''.join(mot_arabe)

if __name__ == "__main__":
      mot = (input("Entrez un mot : ")).lower()
      print(conv_lett(mot))

