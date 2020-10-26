import numpy as np
import cv2 

def boxFilter(imagem):
    # GUARDAR A LINHA COM BLURR JA CALCULADO
    blurColum = []
    # blurr image
    blur_image = []
    # tamanho da linha  imagem
    tamLinhas = imagem.shape[0]
    # tamanho da coluna da imagem
    tamColunas = imagem.shape[1]
    # iteradores
    row = 0
    colum = 0

    while row < tamLinhas:
        while colum < tamColunas:
            media = imagem[row:2+row, colum:2+colum]
            newPixel = round(media.mean())
            colum = colum + 2
            blurColum.append(newPixel)
        blur_image.append(blurColum)
        blurColum = []
        row +=1
        colum =0

    return np.array(blur_image, dtype=np.uint8)




def main():
    img1 = cv2.imread("cr7500x500.png", 0)
    

    # pos box filter
    filtrado = boxFilter(img1)

    cv2.imshow('image1 - filtrada',filtrado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()