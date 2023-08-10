#条件：試行回数は15回　人数は300人
#社会学習のグラフを作る　できたら個人学習も

#やりたいこと　299人が従来型　1人が雑種型でスタート
# 一回の試行で300人全員がランダムに1人選びその人が雑種型なら自分も雑種型になる
# これを15回繰り返す

# 初期値の設定方法がわからない
# csvファイルがいるのか？？

# import matplotlib as mpl
# import matplotlib.pyplot as plt

#なんか前にCSVをダウンロードするのやったな


import numpy as np
import matplotlib.pyplot as plt
from random import randint

year = 15
zasyu_init = 1
zasyu = 1
num_farmer = 300

X = np.array([x for x in range(year)])
number = np.empty(year)

for y in range(year):

    for i in range(num_farmer - zasyu):
        parent = randint(1,num_farmer)
        if y == 0:
            if parent <= zasyu_init:
                zasyu = zasyu + 1
            number[y] = zasyu
            break
        if parent <= number[y-1]:
            zasyu = zasyu + 1
    number[y] = zasyu



print(number)
print(X)

# plt.plot(X, number/num_farmer) # 折れ線グラフをプロット

# plt.title('Transition of corn version')          # 図のタイトル
# plt.xlabel('year')                            # x軸のラベル
# plt.ylabel('frequency')                               # y軸のラベル

# plt.show()

import copy
from tqdm import tqdm

#しゅくだい
frequency = number/num_farmer
fig, ax = plt.subplots()

ratio_mean = np.array([frequency[:, i].mean() for i in range(year)])
print(ratio_mean)
ax.plot(X, ratio_mean, linewidth=5, color="cyan")

#runがいる