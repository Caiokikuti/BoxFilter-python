import numpy as np
import cv2
import sys 
import os
from skimage.transform import resize

def boxFilter(imagem, taxa):
    # GUARDAR A COLUNA COM BLURR JA CALCULADO
    blurRow = []
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
            media = imagem[row:taxa+row, colum:taxa+colum]
            newPixel = round(media.mean())
            colum = colum + taxa
            blurRow.append(newPixel)
        blur_image.append(blurRow)
        blurRow = []
        row +=taxa
        colum =0

    return np.array(blur_image, dtype=np.uint8)




def main():
    if (len(sys.argv)!=3): 
        print("Error, Try like this: python boxfilter.py <nome_do_arquivo_de_imagem.png> <TAXA DE REDUÇÃO>")
        sys.exit()
    
    # os.mkdir('./OUTPUT1')
    path ='./'
    # Abrindo a imagem
    nomeImagem = str(sys.argv[1])
    taxa = int(sys.argv[2])
    img1 = cv2.imread(nomeImagem, 0)
    #Downsampling simples
    downsampling = img1[::int(taxa),::int(taxa)]
    # box filter
    filtrado = boxFilter(img1, taxa)

    #Voltando ao tamanho normal BOX FILTER
    upsamplingBOX = resize(filtrado, (img1.shape[0], img1.shape[1]))
    upsamplingBOX = cv2.convertScaleAbs(upsamplingBOX, alpha=(255.0))
    cv2.imwrite(os.path.join(path ,'BOXFILTERED'+str(taxa)+nomeImagem), upsamplingBOX)
    
    #Voltando ao tamanho normal downsampling
    upsamplingDOWN = resize(downsampling, (img1.shape[0], img1.shape[1]))
    upsamplingDOWN = cv2.convertScaleAbs(upsamplingDOWN, alpha=(255.0))
    cv2.imwrite(os.path.join(path ,'DOWNSAMPLED'+str(taxa)+nomeImagem), upsamplingDOWN)
 
if __name__ == "__main__":
    main()