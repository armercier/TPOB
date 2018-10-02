import matplotlib.pyplot as plt

pixels = []
intensity = []

#READ FILE
valuePairs = [line.rstrip('\n') for line in open('donnees/mercure_etalon.TXT')]
valuePairs.pop()
for i in valuePairs:
    values = i.split(',')
    pixels.append(int(values[1]))
    intensity.append(int(values[2]))

intensityNorm = [x / max(intensity) for x in intensity]

plt.plot(pixels, intensityNorm)
plt.show()
print(pixels)
print(intensity)
