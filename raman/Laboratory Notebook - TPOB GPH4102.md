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

   [Lien vers graphique](https://github.com/SebJercz/TPOB/blob/master/fig/raman/noisevsphotons.png)

   La datasheet parle uniquement de bruit statique

   Pour le PIXIS 100-B, 2 vitesse d'acquisitions sont possibles

   - 100kHz: 3e- rms (typical), 5e- rms (max)
   - 2 MHz: 11e- rms (typical), 16e- rms (max)

   Si on assume que le bruit est un signal sinusoidal, le peak sera à $$\sqrt{2}\cdot U_{rms}$$

   le bruit relatif à la mesure à 80 degré celsius est de 0.001, ce qui explique la pente du graphique

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

**info avec Simon Rainville: **

Fluorescence : Phénomène de résonance, seulement à une longueur d'onde précise, Raman scatter peut arriver peut importe la longueur d'onde mais beaucoup moins intense et cause un moins grand shift de longueur d'onde.

Le raman scattering produit tres peu de signal, alors il faut bien gérer le bruit.

Trois type de bruits : 

* Lecture : Constant peu importe temps d'intégration, "taxe" sur lecture du pixel
* Thermique : Taux/probabilité que capteur génere un électron a cause de température -> +temp = +taux, bruit est linéaire en fonction du temps
* Shot noise : Bruit sur lecture (moyenne 100phot/s, peut mesure autre chose que 1000) : un source lumineuse qui envoie des photons suit la distribution de poisson -> bruit sur nb de photons = sqrt(nb photons). SNR = N/sqrt(N) = sqrt(N)



#### Manipulations ####

**Exploration du montage** 

Parties importantes du montage :

* Notch filter : permet de bloquer la longueur d'onde 632.8nm qui pourrait provenir de la diffusion ou de la Rayleigh scattering. Bloque les longueur d'onde avec son épaisseur, alors important que la lumière arrive perpendiculaire -> on utilise des lentilles avant pour colimer la lumière.
* Fente verticale : permet d'avoir un faisceau le plus ponctuel possible afin d'avoir des pics tres mince sur le spectre et pour éviter l'overlap de certains pics. Plus la fente est petite, plus le signal est "sharp" mais plus on perd de signal
* f

#### Caractérisation du bruit de lecture ####

On enregistre des données ASCII pour différents temps d'intégration pour identifier les bruit de lecture

| **Temps d'intégration** (ms) | Nom du fichier     |
| ---------------------------- | ------------------ |
| 100                          | bruit_mesure_100ms |
| 75                           | bruit_meusre_75ms  |
| 50                           | bruit_meusre_50ms  |
| 25                           | bruit_meusre_25ms  |
| 10                           | bruit_meusre_10ms  |
| 5                            | bruit_meusre_5ms   |
| 1                            | bruit_meusre_1ms   |
| 0.1                          | bruit_meusre_100us |
| 0.001                        | bruit_meusre_1us   |

~~**Observations : ** L'intensité mesurée est toujours autour de 61400, ce qui veut dire qu'une bonne partie du signal capté est uniquement le bruit de lecture?~~  Avec la fonction binning, l'axe des Y n'est pas divisé par le nombre de pixel vertical (100 dans notre cas). On a donc des valeurs qui oscillent autour de 614 pour chaque pixel peu importe le temps d'intégration. 

Après l'échange avec Daniel, different settings de la caméra ont été changé (changé en mode low noise et fréquence 2GHz). Ces données ont donc dues être reprise avec ces settings

Nombre de COUNTS : 

#### Caractérisation du bruit thermique ####

On enregistre des données ASCII pour différents temps d'intégration pour identifier le bruit thermique

| **Temps d'intégration** (s) | Nom du fichier       |
| --------------------------- | -------------------- |
| 1                           | bruit_thermique_1s   |
| 10                          | bruit_thermique_10s  |
| 50                          | bruit_thermique_50s  |
| 100                         | bruit_thermique_100s |

**Observations : **On remarque que prendre des mesures avec les lampes allumées faisait apparaitre des pics dans le spectre obtenu, il a donc fallu s'assurer de bien tout eteindre. Toutefois, des pics etaient toujours présents dans les images, surtout pour 50 et 100 secondes

Après l'échange avec Daniel, different settings de la caméra ont été changé (changé en mode low noise et fréquence 2GHz). Ces données ont donc dues être reprise avec ces settings

Afin de s'assurer que les données mesurées proviennent vraiement du bruit thermique, les mesures seront fait ou le filtre coupe la lumiere vers 632nm, alors on sait que l'augmentation du signal va provenir du temps d'intégration et du bruit thermique

Nombre de COUNTS : 

**Analyse: **  





#### Caractérisation du bruit de photon 	####

On enregistre des données ASCII pour différents temps d'intégration pour identifier le bruit de photon

| **Temps d'intégration** (s) | Nom du fichier          |
| --------------------------- | ----------------------- |
| 0.001                       | bruit_grenaille_1ms     |
| 0.1                         | bruit_grenaille_100ms   |
| 1                           | bruit_grenaille_1s      |
| 5                           | bruit_grenaille_5s      |
| 10                          | bruit_grenaille_10s     |
| ~~50~~                      | ~~bruit_grenaille_50s~~ |

**Observations : ** Forme générale du spectre reste la même

gossage avec Daniel : 

bruit de mesure  79500

80300 ± 150 pour 30ms

80850 ± 150 pour 60ms

85200 ± pour 240ms

Pour que laugmentation du signal soit linéaire, il faut donc soustraire le bruit de mesure. (et aussi le bruit thermique?) Pour le bruit de photon, on peut également considérer une zone du spectre ou l'intensité est constante (pixel 980 et 1020) pour caractériser la moyenne et l'écart type du signal obtenu afin d'éviter de prendre de tres longues acquisisitons

Counts:

**Analyse: **



#### Étalonnage de la caméra sur l’axe des longueurs d’onde ####

Trois gros pics, creux = 



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