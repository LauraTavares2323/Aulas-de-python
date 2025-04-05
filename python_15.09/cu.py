import tkinter as tk
from tkinter import messagebox

def inicio():

    def comprar_racao():
        import tkinter as tk
from tkinter import messagebox

def comprar_racao(dinheiro):
    def comprar_pedigree():
        nonlocal dinheiro
        dinheiro -= 62
        if dinheiro <= 0:
            messagebox.showinfo("Game Over", "Você ficou sem dinheiro e morreu")
            janela_racao.destroy()

    def comprar_quatree():
        nonlocal dinheiro
        dinheiro -= 62
        if dinheiro <= 0:
            messagebox.showinfo("Game Over", "Você ficou sem dinheiro e morreu")
            janela_racao.destroy()

    janela_racao = tk.Toplevel()
    janela_racao.title("Escolha a Ração")

    label = tk.Label(janela_racao, text="Antes de tudo, compre a ração para o seu animal, ambas do mesmo valor (R$62)")
    label.pack()

    botao_pedigree = tk.Button(janela_racao, text="Pedigree", command=comprar_pedigree)
    botao_pedigree.pack()

    botao_quatree = tk.Button(janela_racao, text="Quatree", command=comprar_quatree)
    botao_quatree.pack()

    janela = tk.Tk()
    janela.title("Planejando a Sua Vida")

    label = tk.Label(janela, text="Ok, vamos planejar a sua vida? Você começa com R$600.000")
    label.pack()

    botao_adotar = tk.Button(janela, text="Adotar um animal", command=None)  # Substitua None pela função apropriada
    botao_adotar.pack()

    botao_casa = tk.Button(janela, text="Comprar uma casa ou apartamento", command=None)  # Substitua None pela função apropriada
    botao_casa.pack()

    janela.mainloop()


    def iniciar_jogo():
        dinheiro = 600000
        lista_animais = ['1', '2', '3', '4']

        janela = tk.Tk()
        janela.title("Planejando a Sua Vida")

        label = tk.Label(janela, text="Ok, vamos planejar a sua vida? Você começa com R$600.000")
        label.pack()

        botao_adotar = tk.Button(janela, text="Adotar um animal", command=adotar_animal)
        botao_adotar.pack()

        botao_casa = tk.Button(janela, text="Comprar uma casa ou apartamento", command=comprar_racao)
        botao_casa.pack()

        janela.mainloop()



janela = tk.Tk()
janela.title("Jogo de Vida")


bemvindo = tk.Label(janela, text="Olá, bem-vindo. Como você gostaria de ser chamado(a)?")
bemvindo.pack()

nome = tk.Entry(janela)
nome.pack()

começar = tk.Button(janela, text="Iniciar Jogo", command=inicio)
começar.pack()

janela.mainloop()
