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
    
    """convert a color in other color"""
    def cvt(self, new_color = cv2.COLOR_BGR2GRAY):
        if isinstance(new_color, CvtColor) or new_color is cv2.COLOR_BGR2GRAY:
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
    def putText(self, text="Hello World",position, font = cv2.FONT_HERSHEY_SIMPLEX, fontSize = 2, color = (0,0,0), epaisseur = 3):        
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
       
        if not isinstance(font, FontText) or font is not cv2.FONT_HERSHEY_SIMPLEX :
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
    
    """stop image"""
    def stop():
        cv2.waitKey()
        cv2.destroyAllWindows()
    

"""Librairies for enum operation"""
from enum import Enum, unique

"""Cvt color opencv4"""
#I have to choose only cvt_color that is most using in opencv4
@unique
class CvtColor(Enum):
    pass


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
    
