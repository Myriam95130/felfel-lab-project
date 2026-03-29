from arabizitns import dico_arabizi

voyelles = ['a', 'e', 'i', 'y', 'o', 'ou', 'u']
consonnes = []

for c in dico_arabizi.keys():
        if c not in voyelles:
            consonnes.append(c)

def phono_tns(mot_arabizi):
    i = 0
    structure = ""
    while i < len(mot_arabizi):
        if mot_arabizi[i] in consonnes:
            structure += "C"
            i += 1
        elif mot_arabizi[i] in voyelles:
            structure += "V"
            i += 1
        else:
            i += 1
    return structure
    
print(phono_tns("yesta3mel"))