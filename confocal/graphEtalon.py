import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib
import numpy as np

pixels = []
intensity = []

#READ FILE
valuePairs = [line.rstrip('\n') for line in open('confocal2/resz.csv')]
valuePairs.pop(0)
for i in valuePairs:
    values = i.split(',')
    pixels.append(float(values[0]))
    intensity.append(float(values[1]))

intensityNorm = [x / max(intensity) for x in intensity]
max = max(intensityNorm)
min = min(intensityNorm)
edge9 = min + 0.9*(max-min)
edge1 = min + 0.1*(max-min)

#SWITCH FROM PIXEL TO
zoom = [2,3,4,5,6,7,8]
x = [1.3, 1.0, 0.92, 0.86, 0.78, 0.77, 0.76]
y = [1.2, 1.0, 0.9, 0.8, 0.75, 0.74, 0.73]
shift = [0.5*(x-11) for x in pixels]
shift2 = shift[0:12] + [shift[19], shift[24], shift[28], shift[32], shift[35]]
enveloppe = intensityNorm[0:12] + [intensityNorm[19], intensityNorm[24], intensityNorm[28], intensityNorm[32], intensityNorm[35]]


# SKIIIIIIIA . boum
majorLocator1 = MultipleLocator(2)                       #gros intervalle axe x
majorFormatter1 = FormatStrFormatter('%d')
minorLocator1 = MultipleLocator(1)                       #petit intervalle axe x
majorLocator2 = MultipleLocator(0.2)                      # gros intervalle axe y
majorFormatter2 = FormatStrFormatter('%.1f')
minorLocator2 = MultipleLocator(0.1)                       #petit intervalle axe y


reflexion = plt.plot(zoom, y, 'k--', marker="s", label = 'Résolution en y')
transmission = plt.plot(zoom, x, 'k', marker="o", markersize=6, markeredgewidth=1, markeredgecolor='k', markerfacecolor='w', label = 'Résolution en x')

plt.gca().xaxis.set_major_locator(majorLocator1)
plt.gca().tick_params(axis='both', labelsize = 14)    #tick size
plt.gca().xaxis.set_major_formatter(majorFormatter1)
plt.gca().xaxis.set_minor_locator(minorLocator1)
plt.gca().yaxis.set_major_locator(majorLocator2)
plt.gca().yaxis.set_major_formatter(majorFormatter2)
plt.gca().yaxis.set_minor_locator(minorLocator2)

plt.axis([0, 10, 0.65, 1.4])
plt.xlabel(r'Zoom', fontsize=14)                        #nom axe x, font size
plt.ylabel(r'Largeur de la ESF [$\mu$m]', fontsize=14)                              #nom axe y, font size
plt.rc('legend', fontsize=12)    # legend fontsize

plt.legend(bbox_to_anchor=(0.69, 0.94), loc=2, borderaxespad=0., frameon=False)               #pos legende
# plt.errorbar(x1, y1, xerr=0.5, yerr=2, fmt='ko', markersize=4, ecolor='k', capsize=2,)
# plt.errorbar(x2, y2, xerr=0.5, yerr=2, fmt='wo', markersize=4, ecolor='k', capsize=2,)
#plt.axhline(y=edge1, color='r', linestyle='-')
#plt.axhline(y=edge9, color='r', linestyle='-')
#plt.savefig("fig1.png", dpi=700)
plt.show()


