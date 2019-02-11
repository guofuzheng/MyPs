# author:guofuzheng
# date  :$
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
from math import *
import numpy as np
from MyPs import Ui_MainWindow
class MyPhotoshop(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPhotoshop, self).__init__()
        self.setupUi(self)
        InitImage = cv2.imread("./init_image.jpeg")
        InitImage = cv2.cvtColor(InitImage, cv2.COLOR_BGR2RGB)
        InitImage = cv2.resize(InitImage, (360,480), interpolation=cv2.INTER_CUBIC)
        InitImage_Qt = QImage(InitImage.flatten(),360, 480, QImage.Format_RGB888)
        self.ShowImage(InitImage_Qt)
        self.ImageToShow = InitImage
        self.ImageToSave = InitImage
        self.OriginImage = InitImage
        self.RotateImage = InitImage
        self.Width = InitImage.shape[1]
        self.Height = InitImage.shape[0]
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.GrayImageButton.clicked.connect(self.GrayImage)
        self.BinaryImageButton.clicked.connect(self.BinaryImage)
        self.SaveFileButton.clicked.connect(self.SaveFile)
        self.LeftRotateImageButton.clicked.connect(self.LeftRotateImage)
        self.show()
    def ShowImage(self,Qimage):
        temp_pixmap = QPixmap.fromImage(Qimage)
        self.Pic.setPixmap(temp_pixmap)
    def OpenFile(self):
        filename = QFileDialog.getOpenFileName(self,'选择图像','','')
        if filename[0]:
            PicToOpen = cv2.imread(filename[0])
            self.ImageToSave = cv2.cvtColor(PicToOpen, cv2.COLOR_BGR2RGB)
            self.OriginImage = cv2.cvtColor(PicToOpen, cv2.COLOR_BGR2RGB)
            self.RotateImage = cv2.cvtColor(PicToOpen, cv2.COLOR_BGR2RGB)
            self.Width = PicToOpen.shape[1]
            self.Height = PicToOpen.shape[0]
            print(self.ComputeShape(self.Width,self.Height))
            PicToOpen = cv2.cvtColor(PicToOpen, cv2.COLOR_BGR2RGB)
            PicToOpen = cv2.resize(PicToOpen,self.ComputeShape(self.Width,self.Height),interpolation=cv2.INTER_CUBIC)
            self.ImageToShow = PicToOpen
            PicToOpen_Qt = QImage(self.ImageToShow.flatten(), self.ComputeShape(self.Width,self.Height)[0],
                                  self.ComputeShape(self.Width,self.Height)[1], QImage.Format_RGB888)
            self.ShowImage(PicToOpen_Qt)
    def SaveFile(self):
        filename=QFileDialog.getSaveFileName(self,'保存图像','','')
        if filename[0]:
            cv2.imwrite(filename[0],self.ImageToSave)
    def GrayImage(self):
        self.ImageToSave = cv2.cvtColor(self.OriginImage,cv2.COLOR_RGB2GRAY)
        Gray = cv2.cvtColor(self.OriginImage,cv2.COLOR_RGB2GRAY)
        Gray= cv2.resize(Gray,self.ComputeShape(self.Width,self.Height),interpolation=cv2.INTER_CUBIC)
        self.ImageToShow = Gray
        Gray_Qt = QImage(Gray.flatten(), self.ComputeShape(self.Width,self.Height)[0],
                         self.ComputeShape(self.Width,self.Height)[1], QImage.Format_Grayscale8)
        self.ShowImage(Gray_Qt)
    def BinaryImage(self):
        Gray = cv2.cvtColor(self.OriginImage,cv2.COLOR_BGR2GRAY)
        print(Gray.shape)
        ret, Binary = cv2.threshold(Gray, 100, 255, cv2.THRESH_BINARY)
        self.ImageToSave = Binary
        Binary = cv2.resize(Binary,self.ComputeShape(self.Width,self.Height),interpolation=cv2.INTER_CUBIC)
        self.ImageToShow = Binary
        Binary_Qt = QImage(Binary.flatten(),self.ComputeShape(self.Width,self.Height)[0],
                           self.ComputeShape(self.Width,self.Height)[1],QImage.Format_Grayscale8)
        self.ShowImage(Binary_Qt)
        return
    def LeftRotateImage(self):
        degree = 90
        # 旋转后的尺寸
        Width = self.RotateImage.shape[1]
        Height = self.RotateImage.shape[0]
        heightNew = int(Width * fabs(sin(radians(degree))) + Height * fabs(cos(radians(degree))))
        widthNew = int(Height * fabs(sin(radians(degree))) + Width * fabs(cos(radians(degree))))
        matRotation = cv2.getRotationMatrix2D((Width / 2, Height / 2), degree, 1)
        matRotation[0, 2] += (widthNew - Width) / 2  # 重点在这步，目前不懂为什么加这步
        matRotation[1, 2] += (heightNew - Height) / 2  # 重点在这步
        Rotated = cv2.warpAffine(self.RotateImage, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
        self.ImageToSave = Rotated
        self.RotateImage = Rotated
        WidthRotated = Rotated.shape[1]
        HeightRotated = Rotated.shape[0]
        print(WidthRotated,HeightRotated)
        print(self.ComputeShape(WidthRotated, HeightRotated))
        Rotated = cv2.resize(Rotated, self.ComputeShape(WidthRotated, HeightRotated), interpolation=cv2.INTER_CUBIC)
        self.ImageToShow = Rotated
        Binary_Qt = QImage(Rotated.flatten(), self.ComputeShape(WidthRotated, HeightRotated)[0],
                           self.ComputeShape(WidthRotated, HeightRotated)[1], QImage.Format_RGB888)
        self.ShowImage(Binary_Qt)
        return
    def ComputeShape(self,Width,Height):
        #这里的想法是先看看图片原本的尺寸，如果宽度较大就以宽度铺满640，如果高度较大就铺满480
        if Width>=Height:
            WidthQt = 640
            HeightQt = round(Height*640/Width)
        else:
            HeightQt = 480
            WidthQt = round(Width*480/Height)
        return int(WidthQt),int(HeightQt)
        # return 316,480
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyPhotoshop()
    app.exec_()
