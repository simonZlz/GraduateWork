#-*- coding:utf-8 -*-

import random

def PepperandSalt(src,pepperPer,saltPer):   #椒盐噪声
    NoiseImg=src
    pepperNum = int(pepperPer*src.shape[0]*src.shape[1])
    saltNum  = int(saltPer*src.shape[0]*src.shape[1])
    for i in range(pepperNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        NoiseImg[randX, randY] = 255
    for i in range(saltNum):
        randX = random.random_integers(0, src.shape[0] - 1)
        randY = random.random_integers(0, src.shape[1] - 1)
        NoiseImg[randX,randY]=0
    return NoiseImg

def GaussianNoise(src,means,sigma):   #高斯噪声
    NoiseImg=src
    X= NoiseImg.shape[0]
    Y = NoiseImg.shape[1]
    for x in range(X):
        for y in range(Y):
            NoiseImg[x,y]=NoiseImg[x,y]+random.gauss(means,sigma)
            if  NoiseImg[x,y]< 0:
                     NoiseImg[x,y]=0
            elif NoiseImg[x,y]>255:
                     NoiseImg[x,y]=255
    return NoiseImg

if __name__ == '__main__':
    for