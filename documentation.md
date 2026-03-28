## 27-03-2026 -- premiers jets de code

Avant de commencer à coder, nous avons repéré les principaux problèmes que pourraient poser certaines lettres au moment de la conversion. Un problème auquel j'ai pensé mais que je n'ai pas réussi à anticiper dans le code : les digrammes.

Nous avons écrit un premier script pour essayer de convertir les caractères, en omettant les complexités linguistiques qui nous préoccuperont à des stades plus évolués du projet. 

**Le code :**

## Version 1 — conversion lettre par lettre
```python
dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', 'h':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'o':'و', 'u':'و', 'i':'ي', 'y':'ي', '2': 'ء'
                 }

def conv_lett(mot):
    mot_arabe = []
    for ch in mot:
        if ch in dico_arabizi.keys():
            ch = dico_arabizi[ch]
            mot_arabe.append(ch)
        elif ch not in dico_arabizi:
            mot_arabe.append(ch)
    return ''.join(mot_arabe)

print(conv_lett("khouya"))
```
*Résultat du print :* ```كهoوyا```

**Problème identifié** : les digrammes (`kh`, `gh`, `sh`, `ch`, `dh`) sont traités comme deux caractères séparés au lieu d'un seul son.

## 28-03-2026 -- Résolution du problème des digrammes 

Le problème des digrammes a été réglé en ramplaçant la boucle for par une boucle while, afin de pouvoir lire 2 lettres à la fois :

```python
dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'u':'و', 'i':'ي', '2': 'ء'}

def conv_lett(mot):
    mot_arabe = []
    i = 0
    while i < len(mot):
        if mot[i:i+2] in dico_arabizi:
            mot_arabe.append(dico_arabizi[mot[i:i+2]])
            i += 2
        elif mot[i] in dico_arabizi:
            mot_arabe.append(dico_arabizi[mot[i]])
            i += 1
        else:
            mot_arabe.append(mot[i])
            i += 1 
    return ''.join(mot_arabe)

print(conv_lett("khouya"))
```
*Résultat du print :* ```خويا```

Le "kh" a bien été converti en "خ" et la transcription a bien été exécutée.
Seulement, comment gérer le problème s'il s'agit d'un 'k' + un '7' retranscrit 'h' par l'utilisateur ?

## PROBLÈMES NON RÉGLÉS

Le convertisseur ne peut pas distinguer le digramme kh (خ) de la séquence k + h --> ك + ح (ex. akhal اكحل). Résoudre cette ambiguïté nécessiterait un lexique de référence.

De plus, le convertisseur ne distingue pas les voyelles longues des voyelles courtes. En arabe, les voyelles courtes ne s'écrivent pas, tandis que les voyelles longues sont représentées par ا, و, ي. En Arabizi, les deux se notent de la même façon (a, i, u). Résoudre cette ambiguïté nécessiterait l'implémentation de règles phonologiques, notamment la contrainte du sukun (= absence de voyelle courte) : deux consonnes portant un sukun ne peuvent pas se suivre en arabe. Par exemple, dans ak7al (اكحل), le a est une voyelle courte qui vient avec le son laryndé, d'où le fait que la lettre précédente porte un sukun. Ainsi elle ne devrait pas être transcrit par un alif ا

Autre problème, les lettres géminées : mm, pp, kk etc.

Les emphatiques toujours. 
