from PIL import Image, ImageFilter
from Imagem import Imagem

#classe filtros:

# Filtro preto e branco 
class B_and_W_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_img = aux.get_img()

            filtered_img = filtered_img.convert('1')

            aux.set_img(filtered_img)

            filtered_img.save("AV#/imagens teste/result(B&W).jpg",)

            return aux

# Filtro cartoon
class Cartoon_filter:

     @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_image = aux.get_img().filter(ImageFilter.SMOOTH_MORE)
            
            aux.set_img(filtered_image)

            filtered_image.save("AV#/imagens teste/result(cartoon).jpg",)
            
            return aux
    
   

# Escala de cinza
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

# Filtro negativo
class Negative_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_image = aux.get_img()
            
            inverted_image = Image.eval(filtered_image, lambda pixel: 255 - pixel)
            
            aux.set_img(inverted_image)
            
            inverted_image.save("AV#/imagens teste/result(negativo).jpg",)
            
            return aux

# Modo contorno
class Contour_filter:
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_image = img.get_img().filter(ImageFilter.CONTOUR)
            
            aux.set_img(filtered_image)
            
            filtered_image.save("AV#/imagens teste/result(contorno).jpg",)
            
            return img

# Modo blurred
class Blurr_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        aux = img
        if img.get_img():
            filtered_image = aux.get_img().filter(ImageFilter.BLUR)
            
            aux.set_img(filtered_image)

            filtered_image.save("AV#/imagens teste/result(blur).jpg",)
            
            return aux



    
