import tkinter as tk
from tkinter import messagebox
 
def clique_botao():
    rotulo.config(text="Botão Clicado!")
 
def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Isso é uma mensagem de exemplo.")
 
janela = tk.Tk()
janela.title("Minha Janela")
 
rotulo = tk.Label(janela, text="Aula hoje!")
botao = tk.Button(janela, text="Clique em Mim")
botao_mensagem = tk.Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
 
rotulo.pack()
botao.pack()
botao_mensagem.pack()
botao.config(command=clique_botao)
 
 
janela.mainloop()