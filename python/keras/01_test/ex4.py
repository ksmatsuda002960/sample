# -*- coding: utf-8 -*-
import numpy as np
from keras.models import Sequential, model_from_json
from keras.layers.core import Dense
from keras.optimizers import RMSprop
import os
import matplotlib.pyplot as plt

def plot_history(history, save_graph_img_path, fig_size_x, fig_size_y):


    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
   
    epochs = range(len(acc))

    # グラフ表示
    plt.figure(figsize=(fig_size_x, fig_size_y))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 17
    plt.subplot(121)

    plt.plot(epochs, acc, 'bo' ,label = 'training acc')
    plt.plot(epochs, val_acc, 'b' , label= 'validation acc')
    plt.title('Training and Validation acc')
    plt.grid()
    plt.legend()

 
    plt.subplot(122)
    plt.plot(epochs, loss, 'bo' ,label = 'training loss')
    plt.plot(epochs, val_loss, 'b' , label= 'validation loss')
    plt.title('Training and Validation loss')
    plt.legend()
    plt.grid()

    plt.savefig(save_graph_img_path)
    plt.close() # バッファ解放

def main():

    SAVE_DATA_DIR_PATH = "/Users/panzer5/github/sample/python/keras/01_test/ex4_data/"
    
    # ディレクトリがなければ作成
    os.makedirs(SAVE_DATA_DIR_PATH, exist_ok=True)


    # 説明変数（訓練用データ、入力データ）の用意
    train_x = np.array([[0.0, 0.0],
                        [1.0, 0.0],
                        [0.0, 1.0],
                        [1.0, 1.0]])
    # 目的変数（正解データ）
    train_y = np.array([[0.0, 0.0],
                        [1.0, 0.0],
                        [1.0, 0.0],
                        [0.0, 0.0]])

    # 検証用データ
    test_x = train_x
    test_y = train_y

    # モデル構築
    model = Sequential()

    # 中間層(入力数:input_dim = 2, ユニット数:units = 3) 
    model.add(Dense(activation='sigmoid', input_dim=2, units=3))

    # 出力層(入力数:input_dim = 3だが、中間層のユニット数と同じなので省略可能, ユニット数:units = 2) 
    model.add(Dense(units=2, activation='sigmoid'))

    # 単純パーセプトロンをコンパイル（勾配法：RMSprop、損失関数：mean_squared_error、評価関数：accuracy）
    model.compile(loss='mean_squared_error', optimizer=RMSprop(), metrics=['accuracy'])

    # 学習（教師データでフィッティング、バッチサイズ：4, エポック数：3000）
    history = model.fit(
                        train_x, 
                        train_y, 
                        batch_size=4, 
                        epochs=3000,
                        validation_data=(test_x, test_y)) # 検証用データ

    plot_history(history, SAVE_DATA_DIR_PATH + "graph.png", 25, 10)

if __name__ == '__main__':
    main()


