# -*- coding: utf-8 -*-
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


N = 512            # サンプル数
dt = 0.01          # サンプリング間隔
t = np.arange(0, N * dt, dt)  # 時間軸

# 窓関数の一例
fw1 = signal.hann(N)             # ハニング窓
fw2 = signal.hamming(N)          # ハミング窓
fw3 = signal.blackman(N)         # ブラックマン窓

# グラフ表示
fig = plt.figure(figsize=(10.0, 8.0))
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# 時間信号（元）
plt.plot(t, fw1, label='fw1(t)')
plt.plot(t, fw2, label='fw2(t)')
plt.plot(t, fw3, label='fw3(t)')
plt.xlabel("Time", fontsize=12)
plt.ylabel("Signal", fontsize=12)
plt.grid()
leg = plt.legend(loc=1, fontsize=15)

plt.savefig('C:/github/sample/python/scipy/window-function/ex1.png')
