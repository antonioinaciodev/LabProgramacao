from tkinter import *
from Imagem import Imagem
from filtros import *
from functools import *
from tkinter import filedialog
from tkinter import ttk

imagem = Imagem()

def bt1_click():
    arquivos = filedialog.askopenfilenames()
    imagem.set_local_img(arquivos[0])
    if arquivos:
        imagem.set_local_img(arquivos[0])
        lb1["text"]=f"Imagem carregada:{arquivos[0]}"
    else:
       lb1["text"]="Nenhum arquivo selecionado."

def bt2_click():
    filtro=cb.get()
    if filtro=="Preto e Branco":
        uxbw = B_and_W_filter.apply_filter(imagem)
        uxbw.show_image()

        lb1["text"]="exibido"

    if filtro=="Escala Cinza":
        auxgray = Gray_scale_filter.apply_filter(imagem)
        auxgray.show_image()
        lb1["text"]="exibido"

    if filtro=="Efeito Blurr":
        auxblurr = Blurr_filter.apply_filter(imagem)
        auxblurr.show_image()

    
    if filtro=="Filtro Negativo":
        auxnegative = Negative_filter.apply_filter(imagem)
        auxnegative.show_image()

    if filtro=="Filtro Contorno":
        auxcontorno = Contour_filter.apply_filter(imagem)
        auxcontorno.show_image()

def bt3_click():
    link = ed.get()
    if link:
        imagem.set_public_img(link)
        lb1["text"]=f"Imagem carregada"


janela = Tk()

janela.title("trabalho final")

lb = Label(janela, text="selecione: ")
lb.place(x=100, y=100)

lb1=Label(janela,text="bem vindo")
lb1.place(x=100,y=220)

bt1 =Button(janela, width=10, text="img local")
bt1.place(x=180,y=100)
bt1["command"] = partial(bt1_click)

lb3 = Label(janela, text="internet:")
lb.place(x=280, y=100)

ed= Entry(janela)
ed.place(x=340, y=100)

bt3 =Button(janela, width=8, text="baixar",command=bt3_click)
bt3.place(x=480, y=95)

bt2 =Button(janela, width=8, text="aplicar",command=bt2_click)
bt2.place(x=250,y=150)

lb2=Label(janela,text="filtros")
lb2.place(x=100,y=130)

listFiltros=["Preto e Branco","Escala Cinza","Efeito Blurr","Filtro Negativo","Filtro Contorno"]

cb=ttk.Combobox(janela,values=listFiltros)
cb.place(x=180,y=130)



janela.geometry("600x600+200+200")

janela.mainloop()
