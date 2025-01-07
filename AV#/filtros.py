from PIL import Image
from Imagem import Imagem

#classe filtros:

#filtro preto e branco 
class B_and_W_filter:
    
    @staticmethod
    def apply_filter(img : Imagem):
        aux = img
        if img.get_img():
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('1')

            aux.set_img(filtered_img)

            filtered_img.save("imagens teste/result.jpg",)

            return aux

#filtro cartoon

#escala de cinza

#filtro negativo 

#modo contorno

#modo blurred
