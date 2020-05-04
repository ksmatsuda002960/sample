# -*- coding: utf-8 -*-
import numpy as np
from keras.models import Sequential, model_from_json
from keras.layers.core import Dense, Dropout
from keras.optimizers import RMSprop
from keras.datasets import mnist
from keras.utils import np_utils, to_categorical
import matplotlib.pyplot as plt
import cv2
import os

def main():
    # 入力画像のパラメータ
    img_width = 28 # 入力画像の幅
    img_height = 28 # 入力画像の高さ
    num_input = int(img_width * img_height)

    # データ格納用のディレクトリパス
    SAVE_DATA_DIR_PATH = "/Users/panzer5/github/sample/python/keras/02_mnist/ex2_data/"

    # 保存したモデル構造の読み込み
    model = model_from_json(open(SAVE_DATA_DIR_PATH + "model.json", 'r').read())

    # 保存した学習済みの重みを読み込み
    model.load_weights(SAVE_DATA_DIR_PATH + "weight.hdf5")

    # カメラ画像の整形
    img = cv2.imread(SAVE_DATA_DIR_PATH + "test.png")

    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU) # 2値化
    th = cv2.bitwise_not(th) # 白黒反転
    th = cv2.GaussianBlur(th, (9,9), 0) # ガウスブラーをかけて補間
    th = cv2.resize(th,(img_width, img_height), cv2.INTER_CUBIC) # 訓練データと同じサイズに整形

    # float32に変換して正規化
    th = th.astype('float32')
    th = np.array(th)/255

    # 一次元配列に変換
    th = th.reshape(1, num_input)

    # 分類機に入力データを与えて予測（出力：各クラスの予想確率）
    predict_y = model.predict(th)

    # 最も確率の高い要素番号（=予想する数字）
    predict_number = np.argmax(predict_y) 

    # 予測結果の表示
    print("predict_y:", predict_y)  # 出力値
    print("predict_number:", predict_number)  # 予測した数字

    """
    predict_y: [[4.8937692e-38 1.5886028e-14 1.0000000e+00 6.0272791e-14 0.0000000e+00
    5.9332115e-33 0.0000000e+00 2.5989594e-25 4.9735018e-26 3.0064353e-35]]
    predict_number: 2
    """

    # 分類機に入力データを与えて予測（出力：クラスラベル）
    predict_classes_y = model.predict_classes(th)
    print("predict_classes_y:", predict_classes_y)  # 予測した数字

    # predict_classes_y: [2]

if __name__ == '__main__':
    main()