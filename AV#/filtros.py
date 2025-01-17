from PIL import Image, ImageFilter, ImageOps
from Imagem import Imagem
import os
from copy import deepcopy

#classe filtros:

#todo tratar possiveis erros colocar try e expect

# Filtro preto e branco 
class B_and_W_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

       
# Filtro cartoon
class Cartoon_filter:

    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        try:
            _aux = deepcopy(img)
            aux = _aux.get_img()
            # Get the original image object
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

                output_dir = "AV/imagens_teste"
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, "result(cartoon).jpg")
                cartoonized_image.save(output_path)

                _aux.set_img(cartoonized_image)
                _aux.set_img_path(output_path)

                return _aux
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

# Escala de cinza
class Gray_scale_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

# Escala de cinza
class Gray_scale_filter:
    
    @staticmethod
    def apply_filter(img : Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

# Filtro negativo
class Negative_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

# Modo contorno
class Contour_filter:
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

# Modo blurred
class Blurr_filter:
    
    @staticmethod
    def apply_filter(img: Imagem) -> Imagem:
        try:
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
        except FileNotFoundError as e:
            return f"Erro: Arquivo ou diretório não encontrado. Detalhes: {e}"
        except OSError as e:
            return f"Erro ao processar ou salvar a imagem. Detalhes: {e}"
        except ValueError as e:
            return f"Erro: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"



    
