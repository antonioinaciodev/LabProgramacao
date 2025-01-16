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
        aux = img.get_img()  # Get the original image object
        if aux:  # Ensure the image exists
            # Step 1: Edge Detection
            edges = aux.convert("L")  # Convert to grayscale
            edges = edges.filter(ImageFilter.FIND_EDGES)  # Detect edges
            edges = ImageOps.invert(edges)  # Invert edges
            edges = edges.point(lambda x: 0 if x < 50 else 255)  # Thresholding

            # Step 2: Color Simplification
            simplified_image = aux.filter(ImageFilter.MedianFilter(size=5))  # Reduce noise
            simplified_image = simplified_image.quantize(colors=64)  # Reduce colors

            # Step 3: Combine Edges and Simplified Image
            simplified_image = simplified_image.convert("RGB")  # Convert back to RGB
            edges = edges.convert("L")  # Ensure edges are grayscale
            cartoonized_image = Image.composite(
                simplified_image, Image.new("RGB", simplified_image.size, (0, 0, 0)), edges
            )

            cartoonized_image.save("C:\\Users\w11\Documents\lab\AV#\cartoon")

            return cartoonized_image
        else:
            raise ValueError("Invalid image provided.")
    
    
   

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



    
