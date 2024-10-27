import numpy as np
import matplotlib.pyplot as plt
# Выполнила Михайловская Светлана
#Задание: 4 d

# Цвет: teal, coral, sandybrown, palegreen.
# Линия: штриховая, сплошная, штриховая, штриховая.
# Толщина: 2, 1, 2, 2.
# Сетка: ☑,☒,☑,☑.
# Сетку сделать пунктирной.

# (A)
# 𝑟 = 𝜃,
# 𝑟 = −𝜃 − 𝜋
# (B) r = sin(11·θ)
# (C) 𝑟 = cos4𝜃/7

t1 = np.linspace(0, 7 * 2 * np.pi, 1000)
t2 = np.linspace(0, 2 * np.pi, 1000)

# (A) r = θ и r = -θ - π
r1 = t1
r2 = -t1 - np.pi

# (B) r = sin(11θ)
r3 = np.sin(11 * t2)

# (C) r = cos(4θ/ 7)
r4 = np.cos(4*t1 / 7)

plt.figure('grafix', figsize=(15, 10))

# График (A)
first = plt.subplot2grid((3, 3), (1, 0), polar=True)
first.plot(r1, t1, color='teal', linestyle='--', linewidth=2)
first.plot(r2, t1, color='teal', linestyle='--', linewidth=2)
first.set_title('(A) r = θ; r = -θ - π')
first.grid(color='gray', linestyle=':', linewidth=1)

# График (B)
second = plt.subplot2grid((3, 3), (1, 1), polar=True)
second.plot(t2, r3, color='coral', linestyle='-', linewidth=1)
second.set_title('(B) r = sin(11θ)')
second.set_yticklabels([])
second.grid(False)

 # График (C)
third = plt.subplot2grid((3, 3), (1, 2), polar=True)
third.plot(t1, r4, color='sandybrown', linestyle='--', linewidth=2)
third.set_title('(C) r = cos(4θ / 7)')
third.grid(color='gray', linestyle=':', linewidth=1)

plt.show()
