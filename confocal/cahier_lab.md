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



#### Résolution z

données : après avoir trouvé le focus, nous avons descendu de quelques microns et avont remonté par step de 500nm. Le noms des fichiers sont donc 00.tif, 05.tif, 10.tif, etc.

Les images initiales commences très foncée est deviennent de plus en plus brillante plus on s'approche du focus. Toutefois, après avoir passé le focus, le images ne redeviennent pas tout a fait noire et on observe des "vagues de signal" sur la plaque. Ceci est probablement du a la plaque de resolution USAF qui n'est pas tout a fait droite et cela peut créer une perte de symétrie et de l'interférence.

Champ de vue : 128x128 um

#### Fluorescence

On remplace l'échantillon USAF par une feuille d'arbre. Étant donné qu'on est maintenant en fluorescence et que le signal de reflectance est plus important que le signal de fluorescence (malgré le miroir dichroique), il est important d'utiliser un filtre passe haut 650 nm pour couper le signal de réflectance.

Il est important d'ajuster la bague sur l'objectif qui prend compte du cover sur l'échantillon. La boite dit que ceux si sont entre 0.13 et 0.17mm d'épais, alors la bague est ajustée a 0.15 ce qui semble donner le meilleur résultat. Après avoir trouvé le focus, il faut mettre le gain et le laser au max pour voir quelques cellules.

ovocite : 0.4484 intervalle de 5 micron. On refait le focus et on prend des images a différentes hauteurs pour faire une reconstruction 3D de l'ovocite. 0.5 micron par pixel et on bouge de 5 micron = voxel depth de 10 