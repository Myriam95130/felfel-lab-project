## 27-03-2026 -- **converter.py** : premiers jets de code

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

1. Création d'un dictionnaire dico_arabizi qui associe chaque caractère arabizi à sa lettre arabe
2. Fonction conv_lett qui parcourt le mot caractère par caractère

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

1. Remplacement de la boucle for par une boucle while avec un index i
2. À chaque position, le code regarde d'abord deux caractères (mot[i:i+2]) avant d'en regarder un seul (mot[i])
3. Si le digramme est dans le dictionnaire --> transcription + i += 2
4. Sinon --> caractère seul + i += 1

Le "kh" a bien été converti en "خ" et la transcription a bien été exécutée.
**Question** : Seulement, comment gérer le problème s'il s'agit d'un 'k' + un '7' retranscrit 'h' par l'utilisateur ?

## Gestion partielle des voyelles

1. Ajout d'une liste voyelles = ['a', 'i', 'y', 'o', 'ou', 'e']
2. Ajout d'une variable booléenne last_CV, True si la dernière lettre traitée portait une voyelle, False sinon :  last_CV = False / last_CV = True
3. Si mot[i] est une voyelle et last_CV == True --> voyelle courte, on ignore (i += 1)
4. Si mot[i] est une voyelle et last_CV == False --< voyelle longue, on transcrit + last_CV = True
5. Si mot[i] est une consonne → on transcrit + last_CV reste inchangé

## Gestion des géminées 

```python
elif mot[i] == mot[i+1]:
            mot_arabe.append(dico_arabizi[mot[i]])
            mot_arabe.append('ّ')
            i += 2
```
1. Ajout d'une condition elif mot[i] == mot[i+1] pour détecter les consonnes doublées
2. Une consonne doublée --> transcription de la consonne + shadda ّ + i += 2

## LIMITES REPÉRÉES 

**Ambiguïté des digrammes :** kh peut être خ ou ك + ح (ex. akhal اكحل). Sans lexique de référence impossible à résoudre.

**Emphatiques** : Les emphatiques s, t, dh sont mappés par défaut sur les non-emphatiques (س، ت، ذ). Les emphatiques (ص، ط، ظ) ne sont pas distinguées à l'oral car en tunisien elles se prononcent souvent de la même façon.

**Voyelles longues vs courtes** : La règle last_CV gère le cas où une voyelle suit immédiatement une autre voyelle (sukun). Mais elle ne gère pas le cas des voyelles entre deux consonnes (ex. drab --> دراب au lieu de درب). Résoudre ce cas nécessiterait un analyseur syllabique complet.

En arabe, les voyelles courtes ne s'écrivent pas, tandis que les voyelles longues sont représentées par ا, و, ي. En Arabizi, les deux se notent de la même façon (a, i, u). Résoudre cette ambiguïté nécessiterait l'implémentation de règles phonologiques, notamment la contrainte du sukun (= absence de voyelle courte) : deux consonnes portant un sukun ne peuvent pas se suivre en arabe. Par exemple, dans ak7al (اكحل), le a est une voyelle courte qui vient avec la laryngée 'ح', d'où le fait que la lettre précédente porte un sukun. Ainsi elle ne devrait pas être transcrit par un alif ا.

**Le schwa tunisien (e) : ** Le 'e' en arabizi représente le schwa tunisien, une voyelle centrale qui n'a pas d'équivalent en arabe standard. Dans le code, il est traité comme une voyelle courte et ignoré lors de la transcription. Cette solution est imparfaite car le schwa peut, dans certains contextes, correspondre à un i ou un a court selon les régions et les mots. Une gestion plus fine nécessiterait là aussi un lexique de référence.

**La hamza :**  mappée par défaut sur ء, mais en tunisien elle peut-être réalisée 'a' --> alif.

**La tāʾ marbūṭa :** La tāʾ marbūṭa transcrite comme ة mais en contexte d'annexion elle se réalise comme ت 't'.

Le convertisseur ne peut pas distinguer le digramme kh (خ) de la séquence k + h --> ك + ح (ex. akhal اكحل). Résoudre cette ambiguïté nécessiterait un lexique de référence.

## Code actuel : 

dico_arabizi = {'a':'ا', 'b':'ب', 't': 'ت', 'j':'ج', '7':'ح', 'h':'ح', '5': 'خ', 'kh' :'خ', 'd':'د', 'dh':'ذ', 'r':'ر', 'z': 'ز', 's':'س', 'ch': 'ش', 'sh': 'ش', '3':'ع', '8':'غ', 'gh':'غ', 'f':'ف', '9':'ق', 'q':'ق', 'k':'ك', 'l':'ل', 'm':'م', 'n':'ن', 'h':'ه','ou':'و', 'o':'و', 'u':'و', 'i':'ي', 'y':'ي', '2': 'ء'
                 }
```python
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

mot = (input("Entrez un mot : ")).lower()
print(conv_lett(mot))
```

## 31-03-2026 -- `syllabizer.py` : Syllabiseur de surface (CV)

### Fonctionnement

Attribue une étiquette `C` (consonne) ou `V` (voyelle) à chaque segment
du mot arabizi, selon l'ordre de priorité suivant :

1. Digrammes consonantiques (`kh`, `gh`...) --> `C` (`i += 2`)
2. Semi-consonnes `y` et `w` en position initiale ou post-consonantique --> `C`
3. Digramme vocalique `ou` --> `V` (`i += 2`)
4. Consonnes simples --> `C`
5. Voyelles simples --> `V`
6. Chiffres (consonnes) --> ajoutées 

### Exemples

| Mot arabizi | Structure CV |
|-------------|-------------|
| `khouya`    | `CVVV`      |
| `yesta3mel` | `CVCCVCCVC` |
| `twensa`    | `CCVCCV`    |
| `ak7al`      | `VCCVC`      |

### Note linguistique importante

L'Arabizi ne note pas la distinction voyelle courte/longue.
Toutes les voyelles (`a`, `e`, `i`, `o`, `u`) sont traitées de façon
identique comme `V`. Cette fonction produit donc une **structure CV
de surface uniquement** et non une représentation phonologique profonde.

## Conventions arabizi

| Arabizi | Arabe | Phonème |
|---------|-------|---------|
| `3`     | ع     | /ʕ/     |
| `7`     | ح     | /ħ/     |
| `q`  ou `9`   | ق     | /q/     |
| `ou`    | و     | /u/ ou /w/|
| `kh` ou `5`   | خ     | /x/     |
| `gh` ou `8`   | غ     | /ɣ/     |
| `ch`    | ش     | /ʃ/     |

## Feuille de route

### Court terme
- [ ] Intégrer `converter.py` et `syllabizer.py` dans un pipeline unifié
- [ ] Ajouter des cas de test couvrant la variation dialectale
- [ ] Enrichir l'inventaire des digrammes dans `converter.py`

### Moyen terme
- [ ] Implémenter la segmentation syllabique selon le
      **Principe du Début Maximum**
- [ ] Gérer les préfixes/suffixes morphologiques
      (patrons de conjugaison verbale)

### Long terme : pistes de recherche
- [ ] Reconnaissance des schèmes morphologiques (`CCC`, `CCVC`, `CCvCC`...)
      pour restituer la distinction voyelle courte/longue sous-jacente au sein des verbes dans un premier temps
- [ ] Croisement avec un lexique arabe annoté (Buckwalter / SAMA)
      pour relier les formes arabizi de surface à des entrées arabes annotées
- [ ] Adaptation d'analyseurs morphologiques de l'arabe standard
      à l'Arabizi dialectal tunisien
- [ ] Étiquetage morpho-syntaxique pour l'Arabizi tunisien

## 04/04/2026 -- corrections sur syllabizer.py et converter.py

## 1. `syllabizer.py` corrections 

### Problèmes identifiés et corrigés

**Bug 1 — ordre des conditions dans `phono_tns()`**
La condition semi-consonne `mot[i] in ['y', 'i', 'w'] and i == 0` était placée après le test voyelle simple, donc jamais atteinte. Correction : remonter le bloc semi-consonne avant le test voyelle.

**Bug 2 -- semi-consonnes `y`/`w`**
`'i'` retiré de la liste des semi-consonnes, en arabizi `i` est toujours vocalique. La condition finale :
```python
elif mot_arabizi[i] in ['y', 'w'] and (i == 0 or structure[-1] == 'C'):
    structure += "C"
    i += 1
```

### Tests validés
```
khouya    → CVVV  ✓
yesta3mel → CVCCVCCVC  ✓
twensa    → CCVCCV  ✓
```
---

## 2. `converter.py` -- corrections et nouvelles règles

### Corrections apportées

**Bug 1 : crash en fin de mot (géminées)**
`mot[i] == mot[i+1]` plantait quand `i` était au dernier caractère. Correction :
```python
elif i+1 < len(mot) and mot[i] == mot[i+1]:
```

**Bug 2 — `last_CV` jamais remis à `False` après consonne**
Sans reset, une voyelle transcrite bloquait toutes les voyelles suivantes même après une consonne. 
Correction : ajouter `last_CV = False` dans le bloc consonne simple.

**Bug 3 — `'w'` absent de `dico_arabizi`**
`KeyError: 'w'` lors du traitement de mots comme `weld`. 
Correction : ajouter `'w':'و'` dans le dictionnaire.

### Nouvelle règle -- semi-consonnes `y`/`w`

`y` et `w` retirés de la liste `voyelles`. Nouveau bloc dédié :

```python
elif mot[i] in ['y', 'w']:
    if i+1 < len(mot):  # pas en fin de mot → consonne
        if mot_arabe and mot_arabe[-1] in ['ا', 'و', 'ي']:
            mot_arabe.pop()  # supprimer la voyelle courte précédente
            last_CV = False
        mot_arabe.append(dico_arabizi[mot[i]])
        last_CV = False
        i += 1
    else:  # fin de mot → voyelle pure
        mot_arabe.append(dico_arabizi[mot[i]])
        last_CV = True
        i += 1
```

**Principe** : `y`/`w` suivi d'une consonne ou en fin de mot = voyelle/diphtongue. 
`y`/`w` pas en fin de mot = consonne, la voyelle courte précédente est supprimée (`pop()`).

### Limites documentées

**Diphtongues**
Impossible de distinguer automatiquement `3ayla` (عايلة, voyelle longue + voyelle longue) de `3aychek` (عيشك, `ay` diphtongue) sans lexique. 

**Tāʾ marbūṭa**
Non gérée : impossible de distinguer un `a` final ordinaire (`marhba` = `مرحبا`) d'un `a` signalant une tāʾ marbūṭa (`3ayla` = `عايلة`) sans lexique.

**Hamza**
En arabe tunisien, la hamza (`2`) tombe souvent et s'assimile dans la voyelle environnante (ex : `3a2ila` = `3ayla`). 
Le converter transcrit `2` → `ء` mais ne gère pas l'assimilation dialectale si jamais l'utilisateur venait à entrer le mot en arabe littéral.

## 3. Lexique parallèle — création

### Structure définie
Création d'un fichier CSV `lexiquetns.csv` avec les colonnes :

```
arabizi | arabe_dialectal | phonétique_AL | arabe_littéral | scheme_vocalique | etiquette_morpho | francais | anglais |
```

### Motivation
- Résoudre les ambiguïtés que les règles seules ne peuvent pas traiter (diphtongues, tāʾ marbūṭa, hamza)
- Construire une ressource annotée pour le tunisien arabizi : inexistante à ce jour
- Base pour un futur modèle de vocalisation automatique

## 4. Pistes de recherche évoquées

- **Transducteurs à états finis (FST)** --> approche plus formelle pour le converter.
- **Reconnaissance de schèmes morphologiques** --> pour restituer la distinction voyelle courte/longue
- **Vocalisation automatique** --> entraîner un modèle seq2seq sur des paires arabizi → arabe vocalisé
- **Lexique comparatif arabe littéraire / tunisien dialectal** --> avec colonnes phonétique IPA, schème, catégorie, traductions

## 5. Décision : Transducteurs à états finis (FST)

### Pourquoi pas maintenant

Le passage aux FST a été envisagé pour formaliser les règles de `conv_lett()`. Cependant la décision est de **reporter** cette étape pour les raisons suivantes :

- Les problèmes actuels (diphtongues, hamza, tāʾ marbūṭa) ne seront **pas résolus** par les FST seuls ; ils nécessitent un lexique dans tous les cas. 

### Ce que les FST résoudraient

La logique de `conv_lett()` est déjà un transducteur informel. Un FST formel permettrait de :
- Rendre les règles plus lisibles et maintenables
- Composer plusieurs transducteurs (normalisation + conversion + vocalisation)
- S'interfacer avec des outils académiques (`foma`, `hfst`)

### Feuille de route FST

1. Finir le lexique TSV --> résout les ambiguïtés actuelles
2. Intégrer la fonction `lookup()` dans `converter.py`
3. Reformuler les règles de `conv_lett()` en FST avec `pynini`

## Auteure
Myriam Ben Hadj Sghaier — M1 TAL INALCO / Sorbonne Nouvelle / Paris Nanterre
