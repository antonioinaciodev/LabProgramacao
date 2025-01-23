from tkinter import *
from tkinter import ttk, filedialog, messagebox
from urllib.parse import urlparse
from Imagem import *
from Filtros import *
import os

class App:
    def __init__(self):
        self.imagem = Imagem()
        self.lista_de_imagens = []
        self.caminho_onde_salvar = None

        # Tela inicial (menu principal)
        self.menu_inicial = Tk()
        self.menu_inicial.title("Filters - Menu")
        self.menu_inicial.geometry("500x650+300+200")
        self.menu_inicial.configure(bg="#e8f1f8", highlightbackground="#000000", highlightthickness=3)

        # Centralização de widgets no menu principal
        frame_menu = Frame(self.menu_inicial, bg="#e8f1f8")
        frame_menu.pack(expand=True)

        Label(frame_menu, text="Filters", font=("Broadway", 32, "bold"), bg="#e8f1f8", fg="#000000").pack(pady=20)

        self.create_button(frame_menu, "Editor", self.abrir_editor, "#4aa3df").pack(pady=10)
        self.create_button(frame_menu, "Exit", self.menu_inicial.destroy, "#ff4d4d").pack(pady=10)

    def abrir_editor(self):
        self.menu_inicial.withdraw()
        self.janela_principal()

    def voltar_menu(self):
        self.janela.destroy()
        self.menu_inicial.deiconify()

    def janela_principal(self):
        self.janela = Tk()
        self.janela.title("Filters - Editor")
        self.janela.geometry("500x650+300+200")
        self.janela.configure(bg="#e8f1f8", highlightbackground="#000000", highlightthickness=3)

        frame_principal = Frame(self.janela, bg="#e8f1f8")
        frame_principal.pack(expand=True, fill=BOTH)

        Label(frame_principal, text="Editor", font=("Broadway", 20, "bold"), bg="#e8f1f8", fg="#000000").pack(pady=10)

        Label(frame_principal, text="Escolha o diretório onde as imagens editadas serão salvas:", font=("Arial", 12), bg="#e8f1f8", fg="#3b6a91").pack(pady=5)
        self.create_button(frame_principal, "Escolher Diretório", self.escolher_diretorio, "#4aa3df").pack(pady=5)

        Label(frame_principal, text="Selecione:", font=("Arial", 12), bg="#e8f1f8", fg="#3b6a91").pack(pady=10)
        self.create_button(frame_principal, "Imagem Local", self.bt1_click, "#4aa3df").pack(pady=5)
        Label(frame_principal, text="OU", font=("Arial", 12, "italic"), bg="#e8f1f8", fg="#3b6a91").pack(pady=5)

        Label(frame_principal, text="Imagem da Internet:", font=("Arial", 12), bg="#e8f1f8", fg="#3b6a91").pack(pady=5)
        self.ed = Entry(frame_principal, font=("Arial", 12), width=30)
        self.ed.pack(pady=5)
        self.create_button(frame_principal, "Baixar", self.bt3_click, "#4aa3df").pack(pady=5)

        Label(frame_principal, text="Filtros:", font=("Arial", 12), bg="#e8f1f8", fg="#3b6a91").pack(pady=10)

        self.listFiltros = [
            "Preto e Branco",
            "Escala Cinza",
            "Efeito Blurr",
            "Filtro Negativo",
            "Filtro Contorno",
            "Filtro Cartoon"
        ]

        self.cb = ttk.Combobox(frame_principal, values=self.listFiltros, font=("Arial", 12), width=25)
        self.cb.set("Selecione:")
        self.cb.pack(pady=5)

        self.create_button(frame_principal, "Aplicar", self.bt2_click, "#4aa3df").pack(pady=10)

        self.create_button(frame_principal, "Voltar ao Menu", self.voltar_menu, "#ffa500").pack(pady=20)

        self.janela.mainloop()

    def create_button(self, parent, text, command, color):
        button = Button(parent, text=text, font=("Arial", 12), width=20, bg=color, fg="white", relief="groove", command=command)
        button.bind("<Enter>", lambda e: button.configure(bg="#1f4e79"))
        button.bind("<Leave>", lambda e: button.configure(bg=color))
        return button

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.scheme) and bool(parsed.netloc)

    def escolher_diretorio(self):
        diretorio = filedialog.askdirectory()
        if diretorio:
            self.caminho_onde_salvar = diretorio
            messagebox.showinfo("Diretório Selecionado", f"Diretório escolhido: {diretorio}")
        else:
            messagebox.showinfo("Erro", "Nenhum diretório escolhido.")

    def bt1_click(self):
        arquivos = filedialog.askopenfilenames()
        if self.caminho_onde_salvar is None:
            messagebox.showwarning("Erro", "O usuário não definiu uma pasta para salvar os arquivos.")
        if not arquivos:
            messagebox.showwarning("Erro", "Por favor, adicione uma imagem ou URL!")
            return

        self.imagem.set_local_img(arquivos[0])

    def bt2_click(self):
        try:
            filtro = self.cb.get()
            resultado = None # modificaçao que eu fiz para tratamento de exceção 

            if not filtro:
                messagebox.showwarning("Erro", "Por favor, selecione um filtro!")
                return
            if not self.imagem.get_img():
                messagebox.showwarning("Erro", "Por favor, carregue uma imagem ou forneça uma URL!")
                return

            if filtro == "Preto e Branco":
                resultado = B_and_W_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
                

            elif filtro == "Escala Cinza":
                resultado = Gray_scale_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
             

            elif filtro == "Efeito Blurr":
                resultado= Blurr_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
                

            elif filtro == "Filtro Negativo":
                resultado = Negative_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
                
            elif filtro == "Filtro Contorno":
                resultado = Contour_filter.apply_filter(self.imagem,self.caminho_onde_salvar)
                
            
            elif filtro == "Filtro Cartoon":
                resultado = Cartoon_filter.apply_filter(self.imagem,self.caminho_onde_salvar)

            elif filtro not in self.listFiltros:
                messagebox.showwarning("Erro", "Por favor, selecione um filtro válido!")
                return
               
            if isinstance(resultado,str):
                messagebox.showerror("Erro", resultado)
            else:
                resultado.show_image()
                messagebox.showinfo("Imagem carregada!", "A imagem foi exibida com o filtro escolhido.")

        except Exception as e:
             messagebox.showerror("+Erro Inesperado", f"Detalhes: {e}")

    def bt3_click(self):
        try:
            link = self.ed.get()

            if not link:
                messagebox.showerror("Erro!", "Nenhum endereço foi passado!")
            else:
                if self.is_valid_url(link):
                    if self.caminho_onde_salvar == None:
                        messagebox.showinfo("Nenhum diretorio escolhido")
                        return
                    if link:
                        self.imagem.set_public_img(link,self.caminho_onde_salvar)
                        messagebox.showinfo("Imagem carregada!", "A imagem escolhida foi carregada com sucesso!")
                else:
                    messagebox.showerror("Erro!", "Endereço inválido!")
                
        except Exception as e:
                messagebox.showerror("Erro Inesperado!", f"Detalhes: {e}")

    def run(self):
        self.menu_inicial.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
