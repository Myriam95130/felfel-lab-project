from arabizitns import dico_arabizi

# Voyelles simples de l'arabizi tunisien (pas de distinction courte/longue)

voyelles = ['a', 'e', 'i', 'y', 'o', 'w', 'u']

# Digramme vocalique : "ou" représente /u/ ou /w/ 

digrammes_vocaliques = ['ou']
consonnes = []

# Construction automatique de la liste des consonnes
# à partir des clés du dictionnaire arabizi,
# en excluant les voyelles simples et les digrammes vocaliques

for c in dico_arabizi.keys():
        if c not in voyelles and c not in digrammes_vocaliques:
            consonnes.append(c)

def phono_tns(mot_arabizi):

    """
    Retourne la structure phonologique de surface d'un mot en arabizi tunisien.
    Chaque caractère est étiqueté C (consonne) ou V (voyelle).
    Note : la distinction voyelle courte/longue n'est pas encodée en arabizi,
    cette fonction produit donc une structure CV de surface uniquement.
    """
     
    i = 0
    structure = ""
    while i < len(mot_arabizi):
       # deboggage : print(f"i={i}, char={mot_arabizi[i]}, mot[i:i+2]={mot_arabizi[i:i+2]}, structure={structure}")

       # Digramme consonantique (ex: kh, gh, ch...)
       
        if mot_arabizi[i:i+2] in consonnes:
            structure += "C"
            i += 2

        # Semi-consonne y/w en position initiale ou post-consonantique

        elif mot_arabizi[i] in ['y', 'w'] and (i == 0 or structure[-1] == 'C'):
            structure += "C"
            i += 1

        # Digramme vocalique "ou"

        elif mot_arabizi[i:i+2] in digrammes_vocaliques:
            structure += "V"
            i += 2 
        
        # Consonne simple

        elif mot_arabizi[i] in consonnes:
            structure += "C"
            i += 1 

        # Voyelle simple 

        elif mot_arabizi[i] in voyelles:
            structure += "V"
            i += 1

        # Caractère non reconnu (chiffres (consonnes) arabizi : 3, 7, 9...)
        
        else:
            i += 1

    return structure
    
user = input("Entrez un mot en arabizi : ")
print(phono_tns(user))