import matplotlib.pyplot as plt

with open("2000IterationsPlotPoints.txt", "r") as file:
    PlotPoints = []
    for line in file:
        line = line.split()
        for number in line:
            line[line.index(number)] = line[line.index(number)].replace(',', '')
            number = number.replace(',', '')
            line[line.index(number)] = int(line[line.index(number)])
        PlotPoints.append(line)

plt.plot(PlotPoints[0], PlotPoints[1], 'o', markersize=1)
plt.xlabel('Number That Appears in Sequence')
plt.ylabel('The Number It First Appears Over')
plt.show()
