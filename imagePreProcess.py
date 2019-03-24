#-*- coding:utf-8 -*-
import os
import cv2

srcImagePath = r'C:\Users\user1\Desktop\dataset\imageDataset\srcImages'
outputImagePath = r'C:\Users\user1\Desktop\dataset\imageDataset\croppedImages'

def cropImage():
    for i in os.listdir(srcImagePath):
        img =  cv2.imread(srcImagePath+'\\'+i,0)
        x,y = img.shape[0:2]
        if x==481 and y==321:
            for j in range(0,3):
                cropped = img[160*j:161*(j+1),107*j:107*(j+1)]
                cv2.imwrite(outputImagePath+'\\'+i,cropped)
        elif x==321 and y==481:
            for j in range(0,3):
                cropped = img[107*j:107*(j+1),160*j:161*(j+1)]
                cv2.imwrite(outputImagePath+'\\'+i,cropped)


def resizeImage():
    for i in os.listdir(srcImagePath):
        img =  cv2.imread(srcImagePath+'\\'+i)
        x,y = img.shape[0:2]
        resized = cv2.resize(img,(int(x/4),int(y/4)))
        cv2.imwrite(outputImagePath+'\\'+i,resized)

if __name__ == '__main__':
    cropImage()