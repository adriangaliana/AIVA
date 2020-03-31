
# Imports necesarios
import numpy as np
import cv2
import tensorflow as tf

class recognize():
    def __init__(self):
        return

    def _validate(self):
        return

    def recognize(self):

        """
        El método reconocedor de imagen devuelve un entero, 1 si la imagen sí se puede reconocer o un 0 si la imagen no
        se puede reconocer.
        """
        return


    def _preprocess(self,image, clip_hist_percent=8):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Se calcula el histograma de la imagen pasada a escala de crises
        hist = cv2.calcHist([gray],[0],None,[256],[0,256])
        hist_size = len(hist)

        ## Corrección del brillo y contraste
        accumulator = []
        accumulator.append(float(hist[0]))
        for index in range(1, hist_size):
            accumulator.append(accumulator[index -1] + float(hist[index]))
        maximum = accumulator[-1]
        clip_hist_percent *= (maximum/100.0)
        clip_hist_percent /= 2.0
        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1
        maximum_gray = hist_size -1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1
        alpha = 255 / (maximum_gray - minimum_gray)
        beta = -minimum_gray * alpha
        new_img = image * alpha + beta
        new_img[new_img < 0] = 0
        new_img[new_img > 255] = 255
        auto_result = new_img.astype(np.uint8)

        ## Corrección del gamma
        invGamma = 1.0 / 0.65
        table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")
        image_preprocessed = cv2.LUT(auto_result, table)

        return image_preprocessed

    def _count(self):
        return

    def _position(self):
        return
