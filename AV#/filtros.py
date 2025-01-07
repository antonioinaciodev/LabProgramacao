from PIL import Image
from Imagem import Imagem

#classe filtros:

#filtro preto e branco 
class B_and_W_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('1')

            aux.set_img(filtered_img)

            filtered_img.save("imagens teste/result.jpg",)

            return aux

#filtro cartoon

#escala de cinza
class Gray_scale_filter:

    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        aux = img
        if img.get_img():
            #fazer uma pequena alteração para que a pessoa posso colocar o nome do arquivo
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('L')

            aux.set_img(filtered_img)

            filtered_img.save("AV#/imagens teste/result(cinza).jpg",)

            return aux


#filtro negativo 

#modo contorno

#modo blurred
