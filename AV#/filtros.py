from PIL import Image, ImageFilter
from Imagem import Imagem
import os
from copy import deepcopy

#classe filtros:

# Filtro preto e branco 
class B_and_W_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('1')

            aux.set_img(filtered_img)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, "result(B&W).jpg")
            filtered_img.save(output_path)
            #arrumar esse esquema de salvar,isso so funciona localmente para nos que estamos fazendo o jogo
            #e não coloque o path puro,pq isso so funciona no seu pc
            aux.set_img_path(output_path)
            #todo isso e uma resolucão temporaria para evitar o erro de um path colado no outro 
            return aux

# Filtro cartoon
class Cartoon_filter:

    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            filtered_image = aux.get_img().filter(ImageFilter.SMOOTH_MORE)
            
            aux.set_img(filtered_image)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, "result(cartoon).jpg")
            filtered_image.save(output_path)

            aux.set_img_path(output_path)

            return aux
    
   

# Escala de cinza
class Gray_scale_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            #fazer uma pequena alteração para que a pessoa posso colocar o nome do arquivo
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('L')

            aux.set_img(filtered_img)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, "result(cinza).jpg")
            filtered_img.save(output_path)

            aux.set_img_path(output_path)

            return aux

# Filtro negativo
class Negative_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            filtered_image = aux.get_img()
            
            inverted_image = Image.eval(filtered_image, lambda pixel: 255 - pixel)
            
            aux.set_img(inverted_image)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)
            
            output_path = os.path.join(output_dir, "result(negativo).jpg")
            inverted_image.save(output_path)

            aux.set_img_path(output_path)
            
            return aux

# Modo contorno
class Contour_filter:
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            filtered_image = img.get_img().filter(ImageFilter.CONTOUR)
            
            aux.set_img(filtered_image)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)
            
            output_path = os.path.join(output_dir, "result(contorno).jpg")
            filtered_image.save(output_path)
            
            aux.set_img_path(output_path)

            return img

# Modo blurred
class Blurr_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = deepcopy(img)
        if img.get_img():
            filtered_image = aux.get_img().filter(ImageFilter.BLUR)
            
            aux.set_img(filtered_image)

            output_dir = "AV/imagens_teste"
            os.makedirs(output_dir, exist_ok=True)

            output_path = os.path.join(output_dir, "result(blur).jpg")
            filtered_image.save(output_path)
            
            aux.set_img_path(output_path)

            return aux



    
