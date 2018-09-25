# Laboratory Notebook - TPOB GPH4102

[TOC]



## Raman Spectroscopy

### Preparation

**Théorie** 

Effet Raman : Lumière intéragie avec les vibrations moléculaires ce qui fait changer l'énergie des photons (différente longueur d'onde).

- Peuvent induire une vibration à la molécule -> perd de l'énergie : Stokes

- Peuvent gagner de l'énergie de vibration -> gagne de l'énergie : Anti-Stokes (moins commun)


Rayleigh scattering : Réemet à la même longueur d'onde. Beaucoup plus important que Raman scatterring alors va falloir utiliser un filtre pour cacher cette longueur d'onde pour bien voir spectre Raman

Raman scattering est très faible, important de réduire ou diminuer le bruit (lecture, bruit de photon et bruit thermique)



**Préalables Laboratoire**

1. Spectre mercure

   [Lien vers données](http://njsas.org/projects/atoms/spectral_lines/1/mercury_nist.html)

   Pics importants (Irel >= 1000) : 404.656, 435.833, 546.074, 614.950, pics moins important vers 690 et 708nm

   Étant donné qu'on va principalement détecter des émissions stokes, Il serait préférable de trouver des pics en haut de 633 nm qui sera la longueur d'onde du laser. Toutefois, il n'y a pas vraiment de pics défini a cette longueur d'onde, alors il sera plus difficile d'étalonner le spectromètre. 

2. Specs caméra + profondeur puits

   [Spec sheet](https://www.princetoninstruments.com/userfiles/files/assetLibrary/Datasheets/Princeton_Instruments_PIXIS_100_rev_5_1_10_22_14.pdf)

   - High sensitivity : 300 ke- (typical), 250 ke- (min)
   - High capacity : 1 Me- (typical), 750 ke- (min)

   Ceci correspond aux deux modes de la caméra qui permet une grande sensibilité ou une grande capacité.

   Nombre de photons nécessaires pour ajouter un électron au well dépend de la *quantum efficiency*

   [Graphique QE en fonction longueur d'onde](https://github.com/SebJercz/TPOB/blob/master/fig/raman/Screenshot%20at%202018-09-24%2013_24_29.png)

   Pour le CCD PIXIS100-B utilisé en laboratoire, cela correspond donc à une quantum efficiency d'environ 96%. Toutefois, les émissions Stokes et antistokes sont à d'autre longueurs d'ondes. Selon différentes recherches, ont peut estimer que les longueurs d'onde mesurées vont varier entre 600 et 750nm. 

   En estimant cette section du graphique comme étant linéaire, on peut calculer la quantum efficiency en fonction de la longueur d'onde. Ceci peut être fait dans [ce document excel (feuille 1)](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=0). 



   Le nombre de photons necéssaire pour faire augmenter le valeur du pixel de 1 dépend du mode de la caméra. Le capteur étant 16 bits donc 65535 valeurs, on obtient :

   - High well sensitivity : $$\frac{300000}{65535}\approx 4.57771$$ électrons par incrémentation de pixel.
   - High well capacity :  $$\frac{1000000}{65535}\approx 15.25902$$ électrons par incrémentation de pixel.



   [Source utile](https://www.ptgrey.com/white-paper/id/10912)

3. Bruit photon p/r nombre photons mesuré

4. fréquence de vibration

   La fréquence Raman $$v​$$ s'obtient en faisait $$v = \frac{1}{632.8nm} - \frac{1}{\lambda (x)}​$$ . Avec $$\lambda (x) = 700\text{nm}​$$, on obtient $$151 7.07​$$ cm$$^{-1}​$$. 

   À l'aide de [ce tableau](https://www.utsc.utoronto.ca/~traceslab/raman%20correlation%20table.pdf), [ce document](http://faculty.sites.uci.edu/chem2l/files/2011/03/RDGVibrationalSpec.pdf) ainsi que d'une [feuille de calcul excel](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=1008896699), il est possible de vérifier à l'avance la longueur d'onde et la fréquence Raman attendue pour différents liens moléculaires. Quelques exemples de liens: C=C émet à environ 707nm, C=O à 711nm, C-O à 680nm.

5. Bruit p/r temps

   [Template de tableau excel lin-log](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=1891590538)

6. Spectres chlorophylle

   [Figure des spectres de la chlorophyle](https://github.com/SebJercz/TPOB/blob/master/fig/raman/absorption.gif) [source](http://www.photosynthesis.ch/fluorescence.htm)

   *Pics d'absorbtion* : 430nm et 662nm

   *Pics d'émission* : 669nm

7. Taux gras huile d'olive

   13.8% saturé, 70% mono-insaturé, 13.2% poly-insaturé


### In Lab



## Confocal microscopy

### Preparation

### In Lab



## Hi-Lo Microscopy

### Preparation

### In Lab



## Optical tweezers

### Preparation

### In Lab



## Oximetry

### Preparation

### In Lab