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
#     image = Image.open("inputs/imgs_gray/"+file)
#     gray_bw = image.point(lambda x: 0 if x<128 else 255, '1')
#     gray_bw.save("inputs/imgs_gray/bw_gray/bw-"+file)

BW_Gray = [file for file in listdir("inputs/imgs_gray/bw_gray") if isfile(join("inputs/imgs_gray/bw_gray", file))]

#variation of structuring elements:square, line and circle
kernel = (
    [[cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)), cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)), cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))]],
    [np.ones((1,3), dtype=np.uint8), np.ones((1,5), dtype=np.uint8), np.ones((1,7), dtype=np.uint8)],
    [disk(3), disk(5), disk(7)]
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
    path = "Outṕuts/"+typeImg+"/Erosion/"+element+"/"+dimension+"/"
    name = nameold+"_ero_"+element+"_"+dimension+".png"

    cv2.imwrite(path+name, img)

def dilateImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.dilate(image, kernel, iterations=1)
    path = "Outṕuts/" + typeImg + "/Dilate/" + element + "/" + dimension + "/"
    name = nameold + "_dil_" + element + "_" + dimension + ".png"

    cv2.imwrite(path + name, img)

def openingImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    path = "Outṕuts/" + typeImg + "/Opening/" + element + "/" + dimension + "/"
    name = nameold + "_op_" + element + "_" + dimension + ".png"
    cv2.imwrite(path+name, img)


def closingImage(image, kernel, typeImg, element, dimension, nameold):
    img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    path = "Outṕuts/" + typeImg + "/Opening/" + element + "/" + dimension + "/"
    name = nameold + "_clo_" + element + "_" + dimension + ".png"
    cv2.imwrite(path + name, img)

def main():
    print("Start...")
    print("Dataset: BW")
    for i in range(len(BW)):
        print("Image = "+BW[i])
        print("\n")
        for j in range(3):
            for k in range(3):
                img = ("inputs/imgs_bw/"+BW[i])
                print("Element = "+str(elements[j]))
                print("Dimension = "+str(dimension[k]))
                print("\n\n")
                erosionImage(img, kernel[j][k], "BW", elements[j], dimension[k], BW[i])


if __name__ == '__main__':
    main()