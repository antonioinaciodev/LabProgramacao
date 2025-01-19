from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from tkinter import ttk
from functools import partial
from Imagem import Imagem
from filtros import *


class App:
    def __init__(self):
        self.imagem = Imagem()
        self.lista_de_imagens = []
        self.caminho_onde_salvar = None

        # Inicialização da janela principal
        self.janela = Tk()
        self.janela.title("Trabalho Final")
        self.janela.geometry("600x600+200+200")

        self.lb_dir = Label(self.janela, text="Escolha o diretório onde as imagens baixadas ou editadas ficarão:")
        self.lb_dir.pack()

        self.bt_dir = Button(self.janela, width=15, text="Escolher Diretório", command=self.escolher_diretorio)
        self.bt_dir.pack()

        # Componentes da interface gráfica
        self.lb1 = Label(self.janela, text="BEM-VINDO!")
        self.lb1.pack()

        Label(self.janela, text="").pack()
        Label(self.janela, text="Selecione: ").pack()

        self.bt1 = Button(self.janela, width=10, text="Imagem local", command=self.bt1_click)
        self.bt1.pack()

        Label(self.janela, text="ou").pack()
        Label(self.janela, text="Internet:").pack()

        self.ed = Entry(self.janela)
        self.ed.pack()

        self.bt3 = Button(self.janela, width=8, text="Baixar", command=self.bt3_click)
        self.bt3.pack()

        Label(self.janela, text="").pack()

        self.lb2 = Label(self.janela, text="Filtros:")
        self.lb2.pack()

        self.listFiltros = [
            "Preto e Branco",
            "Escala Cinza",
            "Efeito Blurr",
            "Filtro Negativo",
            "Filtro Contorno",
            "Filtro Cartoon"
        ]

        self.cb = ttk.Combobox(self.janela, values=self.listFiltros)
        self.cb.pack()

        self.bt2 = Button(self.janela, width=8, text="Aplicar", command=self.bt2_click)
        self.bt2.pack()

        Label(self.janela, text="").pack()

        self.bt4 = Button(self.janela, width=8, text="Sair", command=self.bt4_click)
        self.bt4.pack()

    def escolher_diretorio(self):
        diretorio = filedialog.askdirectory()
        if diretorio:
            self.caminho_onde_salvar = diretorio
            messagebox.showinfo("Diretório Selecionado", f"Diretório escolhido: {diretorio}")
        else:
            messagebox.showinfo("Nenhum diretorio escolhido")

    def bt1_click(self):
        arquivos = filedialog.askopenfilenames()
        if not arquivos:
            self.lb1["text"] = "Nenhum arquivo selecionado."
            messagebox.showwarning("Erro", "Por favor, adicione uma imagem ou URL!")
            return

        self.imagem.set_local_img(arquivos[0])
        self.lb1["text"] = f"Imagem carregada: {arquivos[0]}"
    #botão que aplica o filtro
    def bt2_click(self):
        filtro = self.cb.get()
        if filtro == "Preto e Branco":
            uxbw = B_and_W_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            uxbw.show_image()

        elif filtro == "Escala Cinza":
            auxgray = Gray_scale_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            auxgray.show_image()

        elif filtro == "Efeito Blurr":
            auxblurr = Blurr_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            auxblurr.show_image()

        elif filtro == "Filtro Negativo":
            auxnegative = Negative_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            auxnegative.show_image()

        elif filtro == "Filtro Contorno":
            auxcontorno = Contour_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            auxcontorno.show_image()
        
        elif filtro == "Filtro Cartoon":
            auxcartoon = Cartoon_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
            auxcartoon.show_image()

        messagebox.showinfo("Imagem carregada!", "A imagem foi exibida com o filtro escolhido.")

    def bt3_click(self):
        link = self.ed.get()
        if self.caminho_onde_salvar == None:
            messagebox.showinfo("Nenhum diretorio escolhido")
        if link:
            self.imagem.set_public_img(link,self.caminho_onde_salvar)
            messagebox.showinfo("Imagem carregada!", "A imagem escolhida foi carregada com sucesso!")
        else:
            messagebox.showinfo("Nenhum endereço foi passado")

    def bt4_click(self):
        self.janela.destroy()

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
