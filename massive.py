import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # 100 случайных чисел для оси X
y = np.random.rand(100)  # 100 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y)

# Кастомизация графика
plt.title("Диаграмма рассеяния для случайных данных")
plt.xlabel("Случайные значения X")
plt.ylabel("Случайные значения Y")

# Показать график
plt.show()
