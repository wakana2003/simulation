from random import randint
import numpy as np

year = 0
zasyu = 1

X = np.array([x for x in range(16)])
number = np.empty(16)

while year<16 :
    for i in range(300 - zasyu):
        Num = randint(1,10)
        if Num <= 1:
            zasyu = zasyu + 1
    number[year] = zasyu
    year = year + 1


print(number)
print(X)

import matplotlib.pyplot as plt
plt.plot(X, number) # 折れ線グラフをプロット

plt.title('Transition of corn version')          # 図のタイトル
plt.xlabel('year')                            # x軸のラベル
plt.ylabel('number')                               # y軸のラベル

plt.show()