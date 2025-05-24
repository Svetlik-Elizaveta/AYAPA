import numpy as np
import matplotlib.pyplot as plt

# Задание 1
x = np.linspace(-10, 10, 100)
y1 = x
y2 = 2 * x
y3 = 3 * x
y4 = x ** 2
y5 = 2 * (x ** 2)
plt.plot(x, y1, label='y = x', color='blue')
plt.plot(x, y2, label='y = 2x', color='red')
plt.plot(x, y3, label='y = 3x', color='green')
plt.plot(x, y4, label='y = x^2', color='orange')
plt.plot(x, y5, label='y = 2 * x^2', color='purple')
plt.xlim(-15, 15)
plt.ylim(-20, 50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Задание 1')
plt.legend()
plt.show()


# Задание 2
num_GP = 5
GP = np.random.rand(num_GP, 2) * 100
num_SP = 10
plt.figure(figsize=(15, 8))
SP = [i + np.random.normal(0, 5, (num_SP, 2)) for i in GP]
CP = np.array([np.mean(i, axis=0) for i in SP])
POG = [np.std(i, axis=0) for i in SP]
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i in range(len(SP)):
    plt.scatter(SP[i][:, 0], SP[i][:, 1], color=colors[i], alpha=0.6, label='Группа точек ' + str(i + 1))
for i in range(len(CP)):
    plt.errorbar(CP[i][0], CP[i][1], xerr=POG[i][0], yerr=POG[i][1], fmt='o', color='black',
                     capsize=5, label='Центральная точка ' + str(i + 1))
plt.scatter(GP[:, 0], GP[:, 1], color='black', marker='X', s=100, label='Начальные точки')
plt.title('Задание 2. График смещенных точек')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend()
plt.axis('equal')
plt.show()

# Задание 3
import matplotlib.pyplot as plt
import random

matan = []
for i in range(5):
    a = random.randint(3, 5)
    matan.append(a)
linal = []
for i in range(5):
    a = random.randint(3, 5)
    linal.append(a)
gos = []
for i in range(5):
    a = random.randint(3, 5)
    gos.append(a)
hist = []
for i in range(5):
    a = random.randint(3, 5)
    hist.append(a)



plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.step(range(len(matan)), matan, 'r', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('Математический анализ')
plt.grid()

plt.subplot(2, 2, 2)
plt.step(range(len(linal)), linal, 'b', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('Линейная алгебра')
plt.grid()

plt.subplot(2, 2, 3)
plt.step(range(len(gos)), gos, 'g', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('ОРГ')
plt.grid()

plt.subplot(2, 2, 4)
plt.step(range(len(hist)), hist, 'm', where='mid', linewidth=2)
plt.ylim(3, 6)
plt.title('История')
plt.grid()

plt.tight_layout()
plt.show()
print((matan, linal, gos, hist))