from Imagem import Imagem
from filtros import *

imagem = Imagem()
imagem.set_public_img(r"https://www.revistaveterinaria.com.br/wp-content/uploads/2018/11/gatinho-preguicoso1.jpg")
aux = Gray_scale_filter.apply_filter(imagem)
aux.show_image()