import matplotlib.pyplot as plt
import numpy as np

pixels = []
intensity = []

#READ FILE
valuePairs = [line.rstrip('\n') for line in open('donnees/substances/ethanol.TXT')]
valuePairs.pop()
for i in valuePairs:
    values = i.split(',')
    pixels.append(int(values[1]))
    intensity.append(int(values[2]))
intensity.pop()
pixels.pop()

intensity = intensity[260:-1]
intensityNorm = [x / max(intensity) for x in intensity]

#SWITCH FROM PIXEL TO
b = [671, 690, 708, 709]
a = [589, 844, 1092, 1106]
z = np.polyfit(a,b,1)
print("{0}x + {1}".format(*z))
print(z[0])

wavelength = [x * z[0] + z[1] for x in pixels]
wavelength = wavelength[260:-1]

plt.plot(wavelength, intensityNorm,'k-')
plt.xlabel("Longueur d'onde [nm]")
plt.ylabel("Intensité normalisée")
plt.show()
