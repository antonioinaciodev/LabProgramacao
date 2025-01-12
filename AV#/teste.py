from Imagem import Imagem
from filtros import *

imagem = Imagem()
imagem.set_public_img(r"https://www.revistaveterinaria.com.br/wp-content/uploads/2018/11/gatinho-preguicoso1.jpg")

#Descomentar apenas a desejada, se não buga :)

# Mostrar filtro B&W
#uxbw = B_and_W_filter.apply_filter(imagem)
#uxbw.show_image()

# Mostrar filtro Cinza
#auxgray = Gray_scale_filter.apply_filter(imagem)
#auxgray.show_image()

# Mostrar filtro Blur
#auxblurr = Blurr_filter.apply_filter(imagem)
#auxblurr.show_image()

# Mostrar filtro Cartoon

# Mostrar filtro Negativo 
#auxnegative = Negative_filter.apply_filter(imagem)
#auxnegative.show_image

# Mostrar filtro Contorno
#auxcontorno = Contour_filter.apply_filter(imagem)
#auxcontorno.show_image()