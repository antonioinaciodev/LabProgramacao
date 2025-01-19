from tkinter import *
from Imagem import Imagem
from filtros import *
from functools import *
from tkinter import filedialog, messagebox
from tkinter import ttk

imagem = Imagem()

def bt1_click():
    arquivos = filedialog.askopenfilenames()
    if not arquivos:
        lb1["text"] = "Nenhum arquivo selecionado."
        messagebox.showwarning("Erro", "Por favor, adicione uma imagem ou URL!")
        return  
    
    imagem.set_local_img(arquivos[0])
    lb1["text"] = f"Imagem carregada: {arquivos[0]}"

def bt2_click():

    filtro=cb.get()
    if filtro=="Preto e Branco":
        uxbw = B_and_W_filter.apply_filter(imagem)
        uxbw.show_image()

    if filtro=="Escala Cinza":
        auxgray = Gray_scale_filter.apply_filter(imagem)
        auxgray.show_image()

    if filtro=="Efeito Blurr":
        auxblurr = Blurr_filter.apply_filter(imagem)
        auxblurr.show_image()

    if filtro=="Filtro Negativo":
        auxnegative = Negative_filter.apply_filter(imagem)
        auxnegative.show_image()

    if filtro=="Filtro Contorno":
        auxcontorno = Contour_filter.apply_filter(imagem)
        auxcontorno.show_image()

    messagebox.showinfo("Imagem carregada!","A imagem foi exibida com o filtro escolhido.")

def bt3_click():
    link = ed.get()
    if link:
        imagem.set_public_img(link)
        messagebox.showinfo("Imagem carregada!","A imagem ecolhida foi carregada com sucesso!")

def bt4_click():
    exit()


janela = Tk()

janela.title("Trabalho Final")

lb1=Label(janela,text="BEM-VINDO!")
lb1.pack()

lb = Label(janela, text="")
lb.pack()

lb = Label(janela, text="Selecione: ")
lb.pack()

bt1 =Button(janela, width=10, text="Imagem local")
bt1.pack()
bt1["command"] = partial(bt1_click)

lb = Label(janela, text="ou")
lb.pack()

lb = Label(janela, text="Internet:")
lb.pack()

ed= Entry(janela)
ed.pack()

bt3 =Button(janela, width=8, text="Baixar",command=bt3_click)
bt3.pack()

lb = Label(janela, text="")
lb.pack()

lb2=Label(janela,text="Filtros:")
lb2.pack()

listFiltros=["Preto e Branco","Escala Cinza","Efeito Blurr","Filtro Negativo","Filtro Contorno"]

cb=ttk.Combobox(janela,values=listFiltros)
cb.pack()

bt2 =Button(janela, width=8, text="Aplicar",command=bt2_click)
bt2.pack()

lb = Label(janela, text="")
lb.pack()

bt4 =Button(janela, width=8, text="Sair",command=bt4_click)
bt4.pack()

janela.geometry("600x600+200+200")

janela.mainloop()
