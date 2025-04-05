import tkinter as tk
from tkinter import messagebox

#janelas

janela = tk.Tk()
janela.title("Fauna")
janela.geometry("600x400")


#fases/defs

def fase1():
    pergunta.config(text="Qual a espécie de animais marinhos que o macho da a luz aos filhotes?")
    botao.config(text="Cavalo marinho", command=fase2)
    botao1.config(text="Arraia", command=morte)
    botao2.config(text="Polvo", command=morte)
    botao3.config(text="Peixe palhaço", command=morte)

 
def fase2():
    pergunta.config(text="Qual desses animais não é um mamífero?")
    botao.config(text="Morcego", command=fase1)
    botao1.config(text="Tartaruga", command=fase3)
    botao2.config(text="Baleia", command=fase1)
    botao3.config(text="Ornitorrinco", command=fase1)

 
def fase3():
    pergunta.config(text="Quantos dentes tem em média um tubarão?")
    botao.config(text="35 dentes", command=fase1)
    botao1.config(text="Em média 3000 dentes", command=fase4)
    botao2.config(text="278 dentes", command=fase1)
    botao3.config(text="1200 dentes", command=fase1)

def fase4():
    pergunta.config(text="Qual a altura de uma girafa adulta?")
    botao.config(text="3,5 Metros", command=fase1)
    botao1.config(text="5,5 Metros", command=fase1)
    botao2.config(text="4,2 Metros", command=fase5)
    botao3.config(text="5,2 Metros",command=fase1)

def fase5():
    pergunta.config(text="Quantos anos em média vive uma tartaruga?")
    botao.config(text="200 anos", command=fase6)
    botao1.config(text="9 meses ", command=fase1)
    botao2.config(text="300 anos", command=fase1)
    botao3.config(text="5 anos", command=fase1)

def fase6():
    pergunta.config(text="O que acontece quando uma estrela do mar perde o braço?")
    botao.config(text="Regenera apenas a metade", command=fase1)
    botao1.config(text="Sangra", command=fase1)
    botao2.config(text="Perde para sempre", command=fase1)
    botao3.config(text="Regenera", command=fase7)

def fase7():
    pergunta.config(text="Qual a principal diferença do crocodilo e do jacaré?")
    botao.config(text="Os seus olhos e caudas", command=fase1)
    botao1.config(text="Meio de reprodução", command=fase1)
    botao2.config(text="A sua cor", command=fase8)
    botao3.config(text="Tamanho do dente", command=fase1)

def fase8():
    pergunta.config(text="Qual a aranha mais letal do mundo?")
    botao.config(text="Viúva negra", command=fase1)
    botao1.config(text="Tarantula", command=fase1)
    botao2.config(text="Armadeira", command=fase9)
    botao3.config(text="Eratigena agrestis", command=fase1)

def fase9():
    pergunta.config(text="Qual o animal mais esperto do mundo?")
    botao.config(text="Elefante", command=fase1)
    botao1.config(text="Macaco", command=fase1)
    botao2.config(text="Border collie", command=fase1)
    botao3.config(text="Golfinho", command=fase10)

def fase10():
    pergunta.config(text="Qual o maior mamífero do mundo?")
    botao.config(text="Baleia", command=fase11)
    botao1.config(text="Rinoceronte", command=fase1)
    botao2.config(text="Girafa", command=fase1)
    botao3.config(text="Elefante", command=fase1)

def fase11():
    pergunta.config(text="Qual afirmações em relação as zebras, é falsa?")
    botao.config(text="Ela conversam por sinais de orelha", command=fase1)
    botao1.config(text="Elas vivem apenas 12 anos", command=fase12)
    botao2.config(text="Ela é da mesma espécie do cavalo", command=fase1)
    botao3.config(text="Existe um padrão de listras", command=fase1)

def fase12():
    pergunta.config(text="Qual o peixe mais rápido do mundo?")
    botao.config(text="Peixe-lua", command=fase1)
    botao1.config(text="Peixe-vela", command=fase13)
    botao2.config(text="Peixe-palhaço", command=fase1)
    botao3.config(text="Peixe-espadarte", command=fase1)

def fase13():
    pergunta.config(text="Qual o nome da espécie do peixe palhaço?")
    botao.config(text="Amphiprion ocellaris", command=fase14)
    botao1.config(text="Coryphaena hippurus", command=fase1)
    botao2.config(text="Astyanax spp", command=fase1)
    botao3.config(text="Boulengerella cuvieri", command=fase1)

def fase14():
    pergunta.config(text="Qual desses animais não está em extinção?")
    botao.config(text="Arara azul", command=fase13)
    botao1.config(text="Onça-pintada", command=fase13)
    botao2.config(text="Jaguatirica", command=vitoria)
    botao3.config(text="Lobo-guará", command=fase13)

#ter dicas em algumas e deixar mais dificil


#vitoria e derrota

def vitoria():
    messagebox.showinfo("Vitória!", "parábens, você ganhou! se considere um biólogo :)")
    janela.destroy()

def morte():
    messagebox.showinfo("Derrota!", "Ooops, você perdeu :(")
    janela.destroy()

def nao_jogar():
    messagebox.showinfo("Até mais!","é uma pena que você não queira jogar, até a proxima :(")
    janela.destroy()
 
#primeira tela

pergunta = tk.Label(janela, wraplength=500, text="Bem vindo ao jogo Fauna, responda a esse quiz e veja o quanto você conhece do mundo animal...")
botao = tk.Button(janela, text="Sim", command=fase1)
botao1= tk.Button(janela, text="Claro", command=fase1)
botao2 = tk.Button(janela, text="Não", command=nao_jogar)
botao3 = tk.Button(janela, text="Negativo", command=nao_jogar)
 
pergunta.pack()
botao.pack()
botao1.pack()
botao2.pack()
botao3.pack()


 
 
janela.mainloop()
