import matplotlib.pyplot as plt

plt.figure()
x1 = [0, 1]
y1 = [1, 0]
x2 = [-1, 0]
y2 = [0, -1]
x3 = [0, -1]
y3 = [1, 0]
x4 = [1, 0]
y4 = [0, -1]
plt.plot(x1, y1, "r", x2, y2, "g", x3, y3, "b", x4, y4, "k")
plt.show()
