

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

   [Graphique QE en fonction longueur d'onde](https://github.com/SebJercz/TPOB/blob/master/raman/fig/raman/Screenshot%20at%202018-09-24%2013_24_29.png)

   Pour le CCD PIXIS100-B utilisé en laboratoire, cela correspond donc à une quantum efficiency d'environ 96%. Toutefois, les émissions Stokes et antistokes sont à d'autre longueurs d'ondes. Selon différentes recherches, ont peut estimer que les longueurs d'onde mesurées vont varier entre 600 et 750nm. 

   En estimant cette section du graphique comme étant linéaire, on peut calculer la quantum efficiency en fonction de la longueur d'onde. Ceci peut être fait dans [ce document excel (feuille 1)](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=0). 



   Le nombre de photons necéssaire pour faire augmenter le valeur du pixel de 1 dépend du mode de la caméra. Le capteur étant 16 bits donc 65535 valeurs, on obtient :

   - High well sensitivity : $$\frac{300000}{65535}\approx 4.57771$$ électrons par incrémentation de pixel.
   - High well capacity :  $$\frac{1000000}{65535}\approx 15.25902$$ électrons par incrémentation de pixel.



   [Source utile](https://www.ptgrey.com/white-paper/id/10912)

3. Bruit photon p/r nombre photons mesuré 

   [Lien vers graphique](https://github.com/SebJercz/TPOB/blob/master/raman/fig/raman/noisevsphotons.png)
   CE GRAPHIQUE N'EST PLUS BON

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

   [Figure des spectres de la chlorophyle](https://github.com/SebJercz/TPOB/blob/master/raman/fig/raman/absorption.gif) [source](http://www.photosynthesis.ch/fluorescence.htm)

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
* Logiciel d'acquisition : winspec32. Nous avons fixé le rate a 2MHz, le readout a low noise et le gain a 1 pour toute lexpérience

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

**Analyse: **  Après laboratoire



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

**Analyse: ** sera faite apres les laboratoires



#### Étalonnage de la caméra sur l’axe des longueurs d’onde ####

Trois gros pics, creux = Pics seront identifiés avec le tableau de pics du mercure afin de changer l'axe de pixels à un axe en longueur d'onde

On remarque que dans les données il y a un "creux " dans le signal, on détermine que c'est le manque de signal causé par le filtre qui bloque le 632.8nm, alors les longueurs d'ondes a droite de ceux creux sont les longueurs d'onde plus élevées (réseau de diffraction en transmission envoie les plus haute longueurs d'onde plus en angle). Les pics visibles sont donc des pics plus haut que 632nm



### Entre les deux périodes ###

Les pics visibles dans le spectre du mercure sont aux valeurs de pixel 589, 844, 1092 et 1106. Selo [le tableau des pics du mercure](http://njsas.org/projects/atoms/spectral_lines/1/mercury_nist.html), il y a des pics du mercure à environ 671, 690, 708 et 709nm. Si on graph ces valeurs, on remarque que que c'est très linéaire, alors les pics ont bien été identifié. On peut faire un polyfit linéaire pour trouver la fonction qui va transformer les valeurs de pixel en longueur d'onde en nm, ce qui donne $$\lambda = 0.07343918330732058x + 627.8355813527794$$ .

[Lien vers spectre mercure](https://github.com/SebJercz/TPOB/blob/master/raman/fig/mercure.png) [Lien vers spectre olive oil](https://github.com/SebJercz/TPOB/blob/master/raman/fig/oliveoil.png)

### Deuxième période ###

Prise du spectre de l'éthanol :

* Au départ seulement une ligne droite autour de la valeur du bruit de lecture
* en ajustant le temps d'intégration (100ms a 5s), on a pu obtenir des pics ayant environ 10000 d'intensité

#### Discussion avec Simon (comment extraire Raman avec bosse de fluorescence)

Spectre de l'huile d'olive montre seulement une grosse bosse (temps intégration a 100ms). Toutefois, le spectre raman est toujours existant, il est toutefois noyé dans le signal de fluorescence. Avec un temps d'intégration trop court, le signal  est moins important que le bruit. Toutefois, plus le temps d'intégration augmente, plus le signal de fluorescence et de spectre Raman va augmenter de facon linéaire, **MAIS** le bruit vais seulement augmenter avec la racine, alors le bruit de la fluorescence p/r au signal va dimminuer, jusqua ce que le signal soit bien visible dans la courbe. Il sera ensuite possible de soustraire la courbe de fluorescence pour avoir seulement le spectre raman. LA plage dynamique (16bits vs 8 bits) est donc très inportante afin de détecter le signal Raman très faible additionné sur le signal de fluorescence beaucoup plus important.



#### Prises de données

| Substance           | Spectrum File             | Integration time[s] | Spectrum accumulation |      |
| ------------------- | ------------------------- | ------------------- | --------------------- | ---- |
| Olive oil           | olive_oil.txt             | 10                  | 180                   |      |
| Sunflower oil       | sunflower_oil.txt         | 60                  | 5                     |      |
| Peanut oil          | peanut_oil.txt            | 10                  | 10                    |      |
| Canola oil          | canola_oil.txt            | 60                  | 10                    |      |
| Corn oil            | corn_oil.txt              | 60                  | 5                     |      |
| Ethanol             | ethanol.txt               | 50                  | 1                     |      |
| Methanol            | methanol.txt              | 180                 | 1                     |      |
| Isopropanol         | isopropanol.txt           | 120                 | 1                     |      |
| Sucrose             | sucrose.txt.              | 120                 | 3                     |      |
| Glycerol            | glucose.txt               | 120                 | 1                     |      |
| A,B,C,D,E,F,G,H,I,J | A.txt, B.txt, C.txt, etc. | 20                  | 1                     |      |

* Gain ajusté à 1, rate a 2MHz et Readout etait Low noise
* Spectrum accumulation : pour les spcetres qui ont de la fluorescence superposée (voir discussion avec Dan)
* On ajuste temps d'exposition pour bien voir les pics
* Substances inconnues : C a utilisé 3 accums, D  8 accums, G 5 accums (tout pour rendre les pics plus précis)

#### Discussion avec Dan

Le signal de la fluorescence est beaucoup plus important que lui de la spectroscopie raman. Les signals se superposent il faut donc assez de signal pour pouvoir distinguer le raman. 

Calculs

olive oil: le signal mixumum atteint apres 100ms d'intégration est 12000. aucun pic de Raman peut être vu.
éthanol (substance pure, pas de fluorescence) pour 50s d' integration, le signal maximal du plus petit pic est de 2500.
Le signal raman est donc de 4 pour un temps de 100ms. Le signal Raman est don 3000 fois plus petit. Le bruit de photon de la fluorescence $$\sqrt{12000}=110$$. Pour considérer que le signal Raman est visible au dessus du bruit, on veut un pic 5x plus gros que le bruit. On peut calculer le temps nécessaire :
$$4*t[ms]/100=5*\sqrt{12000*t/100}$$
isolant t, on obtient 30min de temps d'intégration. En utilisant la fonction d'accumulation de Winspec, on peut faire plusieurs acquisitions qui seront additionnées pour éviter la saturation d'une intégration continue de 30min.

Forme de bosse dérrière les spectre raman des substance A a J = un peu de fluorescence

il a été discuté que les pics élevé autour du filtre sont du a l'allignement imparfait du système 4f qui collecte la lumiere de l'échantillon



## Confocal microscopy

Dates : 16 et 25 octobre 2018

But principal : calculer la résolution xy et z d'un microscope confocal

### Preparation

Microscope confocal : permet d'uniquement détecter la lumiere qui provient du plan focal à l'aide d'un sténopé, ce qui permet d'observer des échantiollons avec une certaine epaisseur sans avoir de flou. Toutefois, il faut balayer l'échantillon car le focus est seulement en un seul point. 

Signal amplifié avec un photomultiplicateur (PMT). Éviter de mettre lumière ambiante directement dans PMT et de ne pas le saturer, toujours commencer avec gain nul.

Fluorescence : molécule absorbe photons a certaine longueur d'onde (spectre d'excitation) et le réemet des photons (spectre d'émission) à des longueurs d'onde plus longues car les photons perdent de l'énergie par vibration (Stokes shift). $\epsilon$ = coefficient molaire, qté de photons absorbés, $\sigma _a$ = section efficace d'absorbtion, $n$ = efficacité quantique

Marqueurs : Molécule endogène, molécules organiques, protéines fluorescentes, points quantiques

Photoblanchiment : durant excitation les molécalues peuvent faire des réaction et perdre leur propriété fluorescente. Eviter les temps d'Acquisition très long.

### In Lab 

#### Observations montage

Photo du montage : 

![](/home/sebastien/Desktop/TPOB/confocal/45596877_1591517120950135_7765746967946199040_n.jpg)

Explication générale : Le signal du laser est envoyé vers une système du galvanomètre qui va rediriger le faisceau. un système 4f est situé après le galvanomètre pour grossir le faisceau afin qu'il remplisse toute l'ouverture numérique de l'objectif. Cela permet  de mieux focaliser la lumière sur l'échantillon et d'avoir la meilleur résolution possible. le signal est déscanné et est envoyé a travers un miroir dichroique puis vers un pinhole qui va bloquer toute la lumière hors focus(ou au moins diminuer son intensité). 

Miroir dichroique : laisse passer la lumière jusqu'à une certaine longueur d'onde, puis la réfléchie. Deuxx problemes : on travail en réfelctance alors la longueur d'onde ne change pas, le laser devrait être réfléchi autant à l'allé et au retour. De plus, la fluorescence réemet de la lumiere a plus haute longueur d'onde (a moins d'Avoir anti-stokes, ce qui n'est pas le cas), alors le miroir devrait encore bloquer la lumière. Ces deux problèmes sont ngéligeable puisque que le miroir n'est pas parfaitement alligné a 45 degré et qu'il n'est pas parfait, donc il y a toujours environ 1% du signal qui le traverse (SPEC SHEET). Ce 1% de signal est toutefois très suffisant pour que le PMT puisse amplifier le signal.

PMT : 

Objectif : [UPLSAPO-40x2](https://www.olympus-lifescience.com/en/objectives/uplsapo/#!cms[tab]=%2Fobjectives%2Fuplsapo%2F40x2)

Bague prend en compte l'épaisseur du cover glass sur l'échantillon, mais la cible USAF qui sera utilisé pour mesurer la résolution n'en a pas, pas trop grave...

 

#### Manipulations

##### Trouver foyer

On met le gain du PMT a zéro. On place une feuille blanche sous l'échantillion et on peut voir le patern de la cible USAF environ au centre pour bien s'enligner. À l'aide de APT user sur l'ordinateur, on déplace la plaque qui a l'échantillon. La projection du patron de calibration sur la feuille de papier va zoomer jusqu'a temps que'on atteigne environ le focus, et l'image va dézoomer. Sachant la position approximative du focus, on augmente le gain jusqu'a ce quon voit le patron sur Scanimage. On peut ensuite descendre le step du moteur et ajuster la position de l'échantillon plus précisement en cherchant l'image avec les patrons les plus visible, en s'assurant de diminuer le gain pour ne pas saturer. Position sur APT user : -0.3922 , V range = 0.5

Oscilloscope : On voit un pic principal important a environ 10V et plusieurs petits pics qui suivent à environ 2V. L'intervalle en temps entre les pics est d'environ 60ns.

#### Résolution xy

Voici un tableau des images utilisée pour caractériser la résolution en x et en y pour différent zooms :

| Groupe et sous-groupe | Zoom | Moyenne | Nom fichier           | Résolution x (pixel, edge 90% a 10%) | Résolution y (pixel, edge 90% a 10%) | Pixel pour 1 ligne + un espace |
| --------------------- | ---- | ------- | --------------------- | ------------------------------------ | ------------------------------------ | ------------------------------ |
| 5-6 (17.54)           | x5   | 20      | edge_g5_l6_x5.tif     | 4.6                                  | 4.2                                  | 94±1                           |
| 7-6 (4.38)            | x8   | 20      | edge_g7_l1_x8.tif     | 6.0                                  | 5.8                                  | 34±1                           |
| 5-6                   | x2   | 20      | pixelres_g5_l6_x2.tif | 2.6                                  | 2.4                                  | 35±1                           |
| 5-6                   | x3   | 20      | edge_g5_l6_x3.tif     | 3.1                                  | 3.0                                  | 52±1                           |
| 5-6                   | x4   | 20      | edge_g5_l6_x4.tif     | 3.7                                  | 3.6                                  | 70±1                           |
| 7-1 (7.81)            | x6   | 20      | edge_g7_l1_x6.tif     | 4.7                                  | 4.5                                  | 47±1                           |
| 7-1                   | x7   | 20      | edge_g7_l1_x7.tif     | 5.3                                  | 5.1                                  | 53±1                           |

Avec ImageJ, on peut ensuite observer le profil des edges des lignes (edge transfer function). De plus, avec les memes images et les specs de la cible USAF, on peut déterminer un pixel en micron.  résolution : largeur de la edge transfer function (90% a 10%) en micron.

Note : ne pas déplacer la plaque avec le "shift " sur ScanImage, cela désaligne les galvo.

edge transfer function : convolution entre psf et notre edge

| Zoom | Champ de vue (um x um) | Résolution x (um) | Résolution y (um) |
| ---- | ---------------------- | ----------------- | ----------------- |
| x2   | 128.3 x 128.3          | 1.3               | 1.2               |
| x3   | 85.2 x 85.2            | 1.0               | 1.0               |
| x4   | 63.8 x 63.8            | 0.92              | 0.90              |
| x5   | 47.7 x 47.7            | 0.86              | 0.80              |
| x6   | 42.5 x 42.5            | 0.78              | 0.75              |
| x7   | 37.3 x 37.3            | 0.77              | 0.74              |
| x8   | 32.3 x 32.3            | 0.76              | 0.73              |

À revoir avec incertitudes!

Graphique avec incertitudes

![](/home/sebastien/Desktop/TPOB/confocal/res_xy2-page-001.jpg)

Résolutions x et y se chevauchent ce qui est normal, semble avoir un plateau vers x6 zoom

#### Résolution z

données : après avoir trouvé le focus, nous avons descendu de quelques microns et avont remonté par step de 500nm. Le noms des fichiers sont donc 00.tif, 05.tif, 10.tif, etc.

Les images initiales commences très foncée est deviennent de plus en plus brillante plus on s'approche du focus. Toutefois, après avoir passé le focus, le images ne redeviennent pas tout a fait noire et on observe des "vagues de signal" sur la plaque. Ceci est probablement du a la plaque de resolution USAF qui n'est pas tout a fait droite et cela peut créer une perte de symétrie et de l'interférence.

Champ de vue : 128x128 um, zoom = x2, vrange = 0.5

Graphique intensité en fonction déplacement en z, 0 = focus, positif = raproche de lobjectif

![Graphique intensité en fonction déplacement en z, 0 = focus, positif = raproche de lobjetif](/home/sebastien/Desktop/TPOB/confocal/res_z-page-001.jpg)

On pense que les creux viennent de l'interférence, alors on peut faire un enveloppe qui les ignore

Quand même non symétrique : aberration sphérique?

#### Fluorescence

On remplace l'échantillon USAF par une feuille d'arbre. Étant donné qu'on est maintenant en fluorescence et que le signal de reflectance est plus important que le signal de fluorescence (malgré le miroir dichroique), il est important d'utiliser un filtre passe haut 650 nm pour couper le signal de réflectance.

Il est important d'ajuster la bague sur l'objectif qui prend compte du cover sur l'échantillon. La boite dit que ceux si sont entre 0.13 et 0.17mm d'épais, alors la bague est ajustée a 0.15 ce qui semble donner le meilleur résultat. Après avoir trouvé le focus, il faut mettre le gain et le laser au max pour voir quelques cellules.

ovocite : 0.4484 intervalle de 5 micron, zoom 1.5 pour voir la cellule au complet. On refait le focus et on prend des images a différentes hauteurs pour faire une reconstruction 3D de l'ovocite. 0.5 micron par pixel et on bouge de 5 micron = voxel depth de 10 

## Hi-Lo Microscopy / Microscopie

### Preparation

#### Hi-Lo

[Lien du résumé de la dernière équipe](https://github.com/SebJercz/TPOB/blob/master/hilo/resumeHiLo.pdf)

**fonctionnement de base de hilo :** 

![](/home/sebastien/Desktop/TPOB/hilo/Screenshot at 2018-11-06 12:43:07.png)

permet de rejeter la lumière hors en combinant une image avec éclairage uniforme et une image a éclairage structuré (pattern, speckle)

**Ce qui a été fait :** principaux éléments du système d'illumination du microscope hilo ont été assemblé, mais certaines composantes doivent etre ajoutée/modifiée

Pièces importantes :

- camera DMK 21AF04

**Plan semaine 1 : ** 

- trouver un diffuseur qui fait des speckles de taille optimale (trouver cette  taille) car plaque de verre et papier nettoyant ne sont pas ideals
- système d'éclairage uniforme (seulement léclairage structuré a été développé)
- relais 4f qui fait passer dia faisceau de 3cm a 6.35mm
- remplacer plaque de verre 4% reflexion par plaque ou cube 50%

#### Microscopie

**Résumé et théorie :** 

![](/home/sebastien/Desktop/TPOB/hilo/kkk 13:03:20.png)

Illumination de kholer:

- pas mettre miroir au plans conjugés, mettre au plan de fourier
- plan image de l'illumination doit avoir un condenseur pour brouiller l'image de la source lumineuse pour illumination uniforme
- vis du condenseur permet de positionner condenseur pour bien le mettre au plan image

Microscopie de phase:

- Permet de produire des images a haut constraste de spécimen transparents
- passage d'une onde dans un spécimen créé un déphasage et donc de l'interférence
- transforme décalage de phase causé par passage dans specimen par changement d'amplitude de la lumière a laide d'une plaque de phase. Interférence entre rayon principal et rayons difractés

**Questions de préparation : **

$$\Delta r \approx 1.22\frac{\lambda}{D}L\approx\frac{0.6\lambda}{\text{NA}}$$

pour lumière vert qui est environ 540nm et NA =1, on a 336nm.

### In Lab semaine 1

**Ajustement du microscope **

1) on voit bel et bien de la lumière qui sort du pied

3) on se place a x10

4) le diaphragme est ouvert et le microscope est mit en position O

5) L'échantillon utilisé est la r`egle et non les bactéries. Avec la grosse vis et puis la petite vis on atteint une image nette

**Ajustement du condensateur :**

Diaphragme de champ fermé au max, vis viagramme de champ = roulette veritcal noire derriere source lumineuse (dur a voir)

Vis pour déplacement vertical du condensateur : petite vis noire en dessous de la plaque. Vis xy, deux vis grise en doussous de celles du diaphragme

on centre polygone diaphragme de champ avec xy et on met au focus avec vis hauteur. on reouvre le diaphgramme a la grosseur du champ de vue, pas plus.

On ajuste le diaphgrame douverture pour avoir un équilibre entre résolution et contraste

**Échantillons vivants** :

Mettre 15 uL sur une lame puis deposser une lamelle de levure et de bactéries (2 lames dfférentes) Lame L  =levures, lame B = bactéries

Levures : Amas de cellules

Levures x40:

![](/home/sebastien/Desktop/TPOB/hilo/lev40.jpg)

Gros amas de cellule, noyau bien visible

Levures x100 avec huile:

![](/home/sebastien/Desktop/TPOB/hilo/lev_100.jpg)

Structure du noyau encore plus visible

On obseve des amas de cellules avec des cellules qui flottent autour, et quelques plus petites particules qui flottent. On observe également des bulles d'aire beaucoup plus grosse que les cellules.

**Bactéries:**

On met l'objectif 40x et lobjectif et ph4. avec la lentille de bertrand on alligne les aneaux du condensateur avec lanneau de phase de l'objectif. a x40 presque rien est visible, mais a x100 on voit des petits organismes qui grouille le long des bordures des bulles d'air. Objetif x100 nécessite de l'huile

Bactéries x40:

![](/home/sebastien/Desktop/TPOB/hilo/bac40.jpg)

On remarque de petits points pâles, surtout près de la bordure noire

Bactéries x100 avec huile::

![](/home/sebastien/Desktop/TPOB/hilo/bac100.jpg)

Les bactéries sont les ptits objets "cylindriques" légèrement plus pâle que le fond. Généralement pred de la bordure de la bulle d'Eau.

La lentille sur la caméra possède quelques saletés et poussières, qui sont visible au premier plan sur toutes les images. Nettoyage de la lentille serait necéssaire

## Optical tweezers

### Preparation

### In Lab



## Oximetry

### Preparation

### In Lab