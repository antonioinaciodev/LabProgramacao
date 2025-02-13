from ImgDownload import Download
from PIL import Image,UnidentifiedImageError
import matplotlib.pyplot as plt

class Imagem:
    def __init__(self):
        self.img_path = None
        self.img = None
   
    def set_local_img(self,path):
        try:
            self.img_path = path
            self.img = Image.open(path)

        except (FileNotFoundError,UnidentifiedImageError) as e:
            return f"erro encontrado: {e}"

    def set_public_img(self,url,path):
        aux = Download(path)
        aux_path = aux.download_img(url)
        if aux_path:
            try:
                self.img_path = aux_path
                self.img = Image.open(aux_path)
            except UnidentifiedImageError as e:
                raise RuntimeError(f"erro encontrado: {e}")
        else:
            raise RuntimeError("Erro ao baixar a imagem. Verifique o link ou o diretório.")

    def get_img_path(self) -> str:
        return self.img_path
    
    def get_img(self) -> Image:
        return self.img
    
    def set_img(self,img):
        self.img = img
    
    def set_img_path(self,path : str):
        self.img_path = path
        
    def show_image(self):
        if self.img:
            try:
                self.img.show() 
            except Exception as e:
                return f"Erro encontrado: {e}"
        else:
            return "Imagem não encontrada"

    def get_img_extension(self) -> str:
        if self.img:
            return self.img_path.split(".")[1]
        else:
            return "imagem vazia"
