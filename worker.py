# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:48:56 2019

@author: Museigen no reverse
"""
import numpy as np
import cv2

class ImageWork:
    """"Work on image"""
    
    """Initialize the image worker"""
    def __init__(self, image):
        self._image = self.operation(image)
    
    """get the dimension of the image"""
    @property
    def dim(self):
        return self._image.shape
    
    """add operation"""
    def __add__(self, other):
        return cv2.add(self._image, other)
    
    """substract operation"""
    def __sub__(self, other):
        return cv2.subtract(self._image, other)
    
    """multiplation operation"""
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._image * other
        else:
            raise Exception("Type de donnée")
     
    """bitwise and operation"""
    def __and__(self, other):
        return cv2.bitwise_and(self._image, other)
    
    """bitwise or operation"""
    def __or__(self, other):
        return cv2.bitwise_or(self._image, other)
    
    """bitwise xor operation"""
    def __xor__(self, other):
        return cv2.bitwise_xor(self._image, other)
    
    """bitwise not operation"""
    def __invert__(self):
        return cv2.bitwise_not(self._image)
    
    """convert a color in other color"""
    def cvt(self, new_color = CvtColor.BGR2GRAY):
        if isinstance(new_color, CvtColor):
            return cv2.cvtColor(self._image, new_color)
        else :
            raise Exception("La couleur sélectionner n'est pas prise en compte")
    
    """Make basic operation about image"""
    def operation(self, name, operation = 'read', grayscale = None):
        if operation == 'read':
            if grayscale == None :
                return cv2.imread(name)
            else :
                return cv2.imread(name,0)
        elif operation == 'write':
            return cv2.imwrite(name, self._image)
        elif operation == 'show':
            return cv2.imshow(name, self._image)
        else:
            print("L'opération que vous avez effectué n'est pas prise en compte")
    
    """Color at the position"""
    def position(self, row = 0, col = 0):
        return self._image[row, col]
    
    """
        split the color of image in Cvt_color
        i can return shape between = [1,3]    
    """
    def split(self):
        return cv2.split(self._image)
    
    """merge image matrix"""
    def merge(self, arr):
        x = Np.convert_arr(arr)
        if self.dim[2] == x.shape[0]:
            return cv2.merge(arr)
        else:
            raise Exception("Vous ne pouvez pas convertir un tableau de {} élément(s) en un autre de {} élément(s)".format(self.dim[2], x.shape[0]))
    
    """put text on my image"""
    def putText(self, text="Hello World",position, font = FontText.SIMPLEX, fontSize = 2, color = (0,0,0), epaisseur = 3):        
        if not isinstance(text, str) :
            raise Exception("Le text entrer n'est pas un chaîne de caractère")
       
        if position == None:
            raise Exception("La position n'est pas defini et elle est requise")
            
        if not isinstance(position, list) or not isinstance(position, tuple) :
            raise Exception("Le type de la variable position est incorrect")
        else:
            position = tuple(position)
           
        if len(position) != 2:
            raise Exception("La position renseigner ne peut-être atteinte")
        
        if not Utility.allInt(postion) :
            raise Exception("Chaque position doit-être un entier naturel")
        
        if position[0] < 0 or position[0] > self.dim[0] or position[1] < 0 or position[1] > self.dim[1]:
            raise Exception("La position choisie ne se trouve pas sur la figure")
       
        if not isinstance(font, FontText):
            raise Exception("La police de texte que vous avez utilisé n'existe pas")
                
        if not isinstance(color, list) or  not isinstance(color, tuple) :
            raise Exception("Le type de la variable position est incorrect")
        else:
            color = tuple(color)

        if len(color) != 3:
            raise Exception("La couleur renseignée ne peut-être utilisé")
        
        if not Utility.allInt(postion) :
            raise Exception("Chaque position doit-être un entier naturel")
        
        if position[0] < 0 or position[0] > 255 or position[1] < 0 or position[1] > 255:
            raise Exception("La couleur choisie est introuvable")
       
        return cv2.putText(self._image, text, position, font, fontSize, color, epaisseur)
    
    """Make translation on image"""
    def translate(x = 0, y = 0):
        T = np.float32([[1,0,x],[0,1,y]])
        if x >= self.dim[0] or y >= self.dim[1]: 
            print("Vous risquez de ne pas voir l'image car elle est peut-être or des limites")
        return cv2.warpAffine(self._image, T, (self.dim[0], self.dim[1]))
    
    """"reszize image size"""
    def resize(ratio, dim, inter = Inter.Area, operation, vector, start):
        if operation == "crop":
            if vector is not None and start is not None:
                if len(vector) == 2 and len(start) == 2 :
                    return self._image[start[1]:vector[1]+start[1], start[0]:vector[0]+start[0]]
                else:
                    raise Exception("Erreur de dimension")
            else:
                raise Exception("Vueillez renseignez les variables")
        elif operation == "up":
            return cv2.pyrUp(self._image)
        elif operation == "down":
            return cv2.pyrDown(self._image)
        else:
            if ratio == None and dim == None:
                raise Exception("Vueillez renseigner les paramètres")
            elif (isinstance(ratio, float) or isinstance(ratio, int)) and dim == None:
                if ratio > 0 :
                    return cv2.resize(self._image, None, fx = ratio, fy = ratio, interpolation = inter)
                else :
                    raise Exception("Impossible d'avoir un ratio pareil")
            elif (isinstance(dim, list) or isinstance(dim, tuple)) and ratio == None :
                if len(dim) == 2 :
                    if dim[0] != 0 and dim[1] != 0 :
                        return cv2.resize(self._image, tuple(dim), interpolation = inter)
                    else:
                        raise Exception("Vous ne pouvez pas redimension cette image avec une valeur de 0")
                else :
                    raise Exception("Vous n'avez pas entrez une bonne dimension pour le tableau")
            else:
                raise Exception("Vous ne pouvez pas utilisé le ratio et defini la largeur et la longueur simultanement")
    
    """Make rotation"""
    def rotation(operation = 'flip', axis = 1, dim, angle, scale = 1):
        if operation == 'flip':
            if axis not in [0,1]:
                raise Exception("Vous avez renseignez un axe indefini")
            else:
                return cv2.flip(self._image, axis)
        elif operation == 'transpose':
            return cv2.transpose(self._image)
        elif operation == 'rotation_matrix':
            if angle  == None:
                raise Exception("Vous devez defini un angle pour la rotation")
            if scale < 0:
                raise Exception("Impossible d'avoir une echelle de cette valeur")
            if isinstance(dim, list) or isinstance(dim, tuple) :
                if len(dim) != 2:
                    raise Exception("Vous n'avez pas entrez une bonne dimension")
                return cv2.getRotationMatrix2D(dim, angle, scale)
            else:
                raise Exception("Veuillez entrer le bon type de données")
        else:
            raise Exception("Operation non definie")
    
    """stop image"""
    def stop():
        cv2.waitKey()
        cv2.destroyAllWindows()
    

"""Librairies for enum operation"""
from enum import Enum, unique

"""Cvt color opencv4"""
@unique
class CvtColor(Enum):
    BGR2GRAY = cv2.COLOR_BGR2GRAY
    BGR2HLS = cv2.COLOR_BGR2HLS
    BGR2HSV = cv2.COLOR_BGR2HSV
    BGR2Lab = cv2.COLOR_BGR2Lab
    BGR2LUV = cv2.COLOR_BGR2LUV
    BGR2RGB = cv2.COLOR_BGR2RGB
    BGR2XYZ = cv2.COLOR_BGR2XYZ
    BGR2YCR_CB = cv2.COLOR_BGR2YCR_CB
    BGR2YUV = cv2.COLOR_BGR2YUV
    GRAY2BGR = cv2.COLOR_GRAY2BGR
    GRAY2RGB = cv2.COLOR_GRAY2RGB
    HLS2BGR = cv2.COLOR_HLS2BGR
    HLS2RGB = cv2.COLOR_HLS2RGB
    HSV2BGR = cv2.COLOR_HSV2BGR
    HSV2RGB = cv2.COLOR_HSV2RGB
    Lab2BGR = cv2.COLOR_Lab2BGR
    Lab2LBGR = cv2.COLOR_Lab2LBGR
    Lab2LRGB = cv2.COLOR_Lab2LRGB
    Lab2RGB = cv2.COLOR_Lab2RGB
    LUV2BGR = cv2.COLOR_LUV2BGR
    LUV2LBGR = cv2.COLOR_LUV2LBGR
    LUV2LRGB = cv2.COLOR_LUV2LRGB
    LUV2RGB = cv2.COLOR_LUV2RGB
    XYZ2BGR = cv2.COLOR_XYZ2BGR
    XYZ2RGB = cv2.COLOR_XYZ2RGB
    YCR_CB2BGR = cv2.COLOR_YCR_CB2BGR
    YCR_CB2RGB = cv2.COLOR_YCR_CB2RGB
    YUV2BGR = cv2.COLOR_YUV2BGR
    YUV2RGB = cv2.COLOR_YUV2RGB
    

"""Font text of opencv4"""
@unique 
class FontText(Enum):
    COMPLEX = cv2.FONT_HERSHEY_COMPLEX
    COMPLEX_SMALL = cv2.FONT_HERSHEY_COMPLEX_SMALL
    DUPLEX = cv2.FONT_HERSHEY_DUPLEX
    PLAIN = cv2.FONT_HERSHEY_PLAIN
    SCRIPT_COMPLEX = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    SCRIPT_SIMPLEX = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    SIMPLEX = cv2.FONT_HERSHEY_SIMPLEX
    TRIPLEX = cv2.FONT_HERSHEY_TRIPLEX
    ITALIC = cv2.FONT_ITALIC


"""interpolation for image resize"""
@unique
class Inter(Enum):
    AREA = cv2.INTER_AREA
    LINEAR = cv2.INTER_LINEAR
    LANCZOS4 = cv2.INTER_LANCZOS4
    NEAREST = cv2.INTER_NEAREST
    CUBIC = cv2.INTER_CUBIC


"""class for Error message"""
class Error:
    pass


"""Utilities for make numpy operations"""
class Np:       
    @staticmethod
    def convert_arr(x):
        if isinstance(x, list):
            x = np.array(x)
            return x
        else :
            raise Exception("Vous ne pouvez pas convertir cet instance en un tableau numpy")
            
            
"""utilities functions"""
class Utility:
    @staticmethod
    def allInt(arr):
        return all([isinstance(item, int) for item in arr])
    
    
