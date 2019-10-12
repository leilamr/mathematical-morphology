#imports
import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join
from skimage.morphology import disk
from PIL import Image, ImageDraw, ImageFont


#structure for saved images output
pathOp = ("Erosion", "Dilate", "Opening", "Closing")
pathTypeImage = ("BW", "Gray")
elements = ("square", "line", "disk")
dimension = ("3", "5", "7")

#names images
BW = [file for file in listdir("inputs/imgs_bw") if isfile(join("inputs/imgs_bw",file))]
Gray = [file for file in listdir("inputs/imgs_gray") if isfile(join("inputs/imgs_gray", file))]

#convert images gray scale to black and white
# for file in Gray:
#     image = cv2.imread("inputs/imgs_gray/"+str(file),0)
#     ret,gray = cv2.threshold(image,127,256,cv2.THRESH_BINARY)
#     cv2.imwrite("inputs/imgs_gray/bw_gray/bw-"+file, gray)

BW_Gray = [file for file in listdir("inputs/imgs_gray/bw_gray") if isfile(join("inputs/imgs_gray/bw_gray", file))]

#variation of structuring elements:square, line and circle
kernel = (
    [[cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))],
    [np.ones((1, 3), dtype=np.uint8), np.ones((1, 5), dtype=np.uint8), np.ones((1, 7),  dtype=np.uint8)],
    [disk(3), disk(5), disk(7)]]
)

#structure to save output images: Output -> typeImg -> typeOp -> element -> dimension kernel
os.makedirs("Outputs/", exist_ok=True)
for img in range(len(pathTypeImage)):
    for op in range(len(pathOp)):
        for el in range(len(elements)):
            for dk in range(len(dimension)):
                os.makedirs("Outputs/"+pathTypeImage[img]+"/"+pathOp[op]+"/"+elements[el]+"/"+dimension[dk], exist_ok=True)


def erosionImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.erode(image, kernel, iterations=1)
    path = "Outputs/"+str(typeImg)+"/Erosion/"+str(element)+"/"+str(dimension)+"/ero_"+str(element)+"_"+str(dimension)+"_"+str(nameold)
    cv2.imwrite(path, img)

def dilateImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.dilate(image, kernel, iterations=1)
    path = "Outputs/" + str(typeImg) + "/Dilate/" + str(element) + "/" + str(dimension) + "/dil_" + str(element) + "_" + str(dimension) + "_" + str(nameold)
    cv2.imwrite(path, img)

def openingImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    path = "Outputs/" + str(typeImg) + "/Opening/" + str(element) + "/" + str(dimension) + "/ope_" + str(element) + "_" + str(dimension) + "_" + str(nameold)
    cv2.imwrite(path, img)


def closingImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    path = "Outputs/" + str(typeImg) + "/Closing/" + str(element) + "/" + str(dimension) + "/clo_" + str(element) + "_" + str(dimension) + "_" + str(nameold)
    cv2.imwrite(path, img)

def main():
    print("Start...")
    print("Dataset: BW")
    for i in range(len(BW)):
        print("\nImage = "+BW[i])
        for j in range(3):
            for k in range(3):
                print("Element = "+str(elements[j]))
                print("Dimension = "+str(dimension[k]))
                img = cv2.imread("inputs/imgs_bw/"+str(BW[i]), 0)
                print("Op: Erosion")
                erosionImage(img, kernel[j][k], "BW", elements[j], dimension[k], BW[i])

                print("Op: Dilate")
                dilateImage(img, kernel[j][k], "BW", elements[j], dimension[k], BW[i])

                print("Op: Opening")
                openingImage(img, kernel[j][k], "BW", elements[j], dimension[k], BW[i])

                print("Op: Closing")
                closingImage(img, kernel[j][k], "BW", elements[j], dimension[k], BW[i])

    print("Dataset: Gray")
    for i in range(len(BW_Gray)):
        print("\nImage = " + BW_Gray[i])
        for j in range(3):
            for k in range(3):
                print("Element = " + str(elements[j]))
                print("Dimension = " + str(dimension[k]))
                img = cv2.imread("inputs/imgs_gray/bw_gray/" + str(BW_Gray[i]), 0)
                print("Op: Erosion")
                erosionImage(img, kernel[j][k], "BW_Gray", elements[j], dimension[k], BW_Gray[i])

                print("Op: Dilate")
                dilateImage(img, kernel[j][k], "BW_Gray", elements[j], dimension[k], BW_Gray[i])

                print("Op: Opening")
                openingImage(img, kernel[j][k], "BW_Gray", elements[j], dimension[k], BW_Gray[i])

                print("Op: Closing")
                closingImage(img, kernel[j][k], "BW_Gray", elements[j], dimension[k], BW_Gray[i])

if __name__ == '__main__':
    main()