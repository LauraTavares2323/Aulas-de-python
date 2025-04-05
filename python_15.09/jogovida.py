from art import *
#boas vindas

import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()

frame = tk.Frame(janela)

coco = tk.Label(janela, text="coco" )
botao = tk.Button(janela, text="ccocoo")

print("Olá, bem vindo. Como você gostaria de ser chamado(a)?")
name = input()
ração = ""
esperar = ""

print("Ok,",name, "vamos planejar a sua vida? Você começa com R$600.000")
dinheiro = 600000
lista_animais = ['1', '2', '3', '4']

while True:
  #jogo
  #animal
  print("Que tal adotar um companheiro?")
  print("1- Sim")
  print("2- Não")
  adotar = input()
  if adotar == "1":
    print("Você foi até uma casa de adoção... agora, escolha seu animal...")
    print("1- cachorro")
    print("2- gato")
    print("3- passáro")
    print("4- coelho")
    while True:
      animal = input()
      if animal in lista_animais:
        print("Qual será o nome do seu companheiro?")
        nome = input()
        print("Antes de tudo, compre a ração para o seu animal, você pode escolher entre duas marcas, ambas do mesmo valor(R$62)")
        print("1- pedigree")
        print("2- quatree")
        ração = input()
        if ração == "1":
          dinheiro -= 62
          if dinheiro <= 0:
            print("Você ficou sem dinheiro e morreu")
            break
        if ração == "quatree":
          dinheiro -= 62
          if dinheiro <= 0:
            print("Você ficou sem dinheiro e morreu")
            break
        print("Agora você tem um amigo para vida! Acho que já esta na hora de um lar para você e",nome, ":)")
        break
      else:
        print("Esse animal não está para a adoção!")
        animal = ''
        print("Escolha novamente")
        continue
  else:
    print("Ok, que tal um apartamento ou uma casa? Vá para a proxima fase e conquiste seu lar.")


  #casa
  casa = ""
  mobilia = ""
  print("Você foi até uma imobiliaria e a atendente te deu duas ofertas, escolha uma delas ou avance para a proxima fase")
  print("1- proxima fase")
  print("2- casa de 500 mil")
  print("3- apartamento de 250 mil")
  casa = input()

  if casa == "1":
    print("Ok, vá para proxima fase")
  else:
    if casa == "3":
      dinheiro -= 250000
      print("Agora seu saldo é de", dinheiro)
      print("Você deseja mobilia-la?")
      print("1- sim")
      print("2- não")
      mobilia = input()
      if mobilia == "1":
        print("Você tem duas opções, pedir ajuda para seus pais (R$2000) ou comprar movèis(R$25000), qual você escolhe?")
        print("1- ajuda")
        print("2- comprar")
        mobilia = input()
        if mobilia == "1":
          dinheiro -=2000
          if dinheiro <= 0:
            print("Você ficou sem dinheiro e morreu")
            break
          print("Agora você tem movèis e o saldo de ", dinheiro)
        if mobilia == "2":
          dinheiro -= 25000
          if dinheiro <= 0:
            print("Você ficou sem dinheiro e morreu")
          print("Após essa compra seu saldo é de", dinheiro)
          print("Você comprou todos seus movèis e sua casa está linda!")

    if casa == "2":
      dinheiro -= 500000
      if dinheiro <= 0:
        print("Você ficou sem dinheiro e morreu")
        break
      print("Agora seu saldo é de", dinheiro)
      print("Você deseja mobilia-la?")
      print("1- sim")
      print("2- não")
      mobilia = input()
      if mobilia == "1":
        print("Você tem duas opções, pedir ajuda para seus pais (R$2000) ou comprar movèis(R$25000), qual você escolhe?")
        print("1- ajuda")
        print("2- comprar")
        mobilia = input()
        if mobilia == "1":
          dinheiro -= 2000
          print("Agora você tem movèis e o saldo de ", dinheiro)
        if mobilia == "2":
          dinheiro -= 25000
          if dinheiro <= 0:
            print("Você ficou sem dinheiro e morreu")
            break
          print("Você comprou todos seus movèis e sua casa está linda!")



  #seguro da casa

    seguro = ""
    if casa !=  "1":
      print("A sua casa precisa de um seguro para caso alguma coisa aconteça. Você quer o seguro (R$1.500) ou prefere ficar sem(R$0)?")
      print("1- seguro")
      print("2- ficar sem")
      seguro = input()
      if seguro == "1":
        dinheiro -= 1500
        print("Após essa compra seu saldo é de", dinheiro)
        if dinheiro <= 0:
          print("Você morreu!")
          break
        print("Agora a sua está casa segura caso algo aconteça")

      if seguro == "2":
        print("Você não tem seguro")

#viver
  comida = ""
  print("Você decidiu jantar por que já são 9 horas da noite. Você quer comprar uma comida pronta ou cozinhar?")
  print("1- comprar")
  print("2- cozinhar")
  comida = input()
  if comida == "1":
    print("Você abriu o ifood e estava em duvida sobre 2 restaurantes, subway e mc donalds. Qual você escolhe?")
    print("1- subway")
    print("2- mc donalds")
    comida = input()
    if comida == "1":
        dinheiro -= 29
        if dinheiro <= 0:
          print("Você ficou sem dinheiro e morreu")
        print("O lanche que você escolheu custou R$24,00, você comeu e aproveitou junto com um refri lata que custou R$5,00")
        print("Após essa compra seu saldo é de", dinheiro)
    if comida == "2":
        dinheiro -= 37
        if dinheiro <= 0:
          print("Você ficou sem dinheiro e morreu")
        print("O lanche que você escolheu custou R$32,00, você comeu e aproveitou junto com um refri lata que custou R$5,00")
        print("Após essa compra seu saldo é de", dinheiro)
  else:
    if comida == "2":
      print("Você foi até a cozinha e viu que tinha apenas duas opções para comer, qual você escolhe.")
      print("1- miojo")
      print("2- lasanha")
      comida = input()

    if comida == "1":
        print("Você encheu uma panela de água, colocou e o miojo. Agora só resta esperar")
        print("Onde você prefere esperar?")
        print("1- cozinha")
        print("2- quarto")
        esperar = input()
        if esperar == "1":
          print("O miojo ficou pronto, você comeu e ficou satisfeito")


        if casa == "1":
          if esperar == "2":
            print("O miojo queimou, a casa pegou fogo e você morreu!")
          break

        if casa == "2" or "3" and esperar =="2":
          if seguro == "2":
            print("A sua casa pegou fogo e você morreu, como não tinha seguro não conseguiu recuperar")
            break
          if seguro == "1":
            print("A sua casa pegou fogo porém você fez o seguro então consegugiu recuperar :)")

    if comida == "2":
        print("Você colocou a lasanha no microondas e agora só resta esperar")
        print("Onde você prefere esperar?")
        print("1- cozinha")
        print("2- quarto")
        esperar = input()
        if esperar == "1":
          print("A lasanha ficou pronta, você comeu e ficou satisfeito")

        if casa == "1":
          if esperar == "2":
            print("A lasanha queimou, a casa pegou fogo e você morreu!")
          break

        if casa == "2" or "3" and esperar =="2":
          if seguro == "2":
            print("A sua casa pegou fogo e você morreu, como não tinha seguro não conseguiu recuperar")
            break
            if seguro == "1":
              print("A sua casa pegou fogo porém você fez o seguro então consegugiu recuperar :)")

#assistir tv
  assistir = ""
  hacker = ""
  ops = ""
  print("Após comer você decidiu assistir algo no computador, como você quer assistir?")
  print("1- site pirata")
  print("2- netflix")
  assistir = input()
  if assistir == "1":
    print("Você assistiu o filme, porém viu que tinha algo errado após terminar")
    print("Você decide ignorar ou ver se tem virus")
    print("1- ignorar")
    print("2- ver se tem virus")
    hacker = input()

    if hacker == "2":
      print("Você achou um virus porém já utilizou o anti-virus")
      print("Depois de verificar que está seguro você deitou na cama e dormiu")
      tprint("Parabéns!!")
      print("Você sobreviveu a um dia de vida e ganhou o jogo")
    if hacker == "1":
      print("Você ignorou e tentou dormir, porém começou a sair uma voz do seu computador")
      print("Era um hacker! e ele ameaçou te matar, o que você faz?")
      print("1- liga para a policia")
      print("2- se esconde")
      ops = input()
      if ops == "1":
        print("Os policiais acharam que era um trote e desligaram, você morreu.")
        break
      if ops == "2":
        print("Você se escondeu porém depois de um tempo alguém bateu na sua porta...")
        print("Você decide fugir ou ver quem é?")
        print("1- fugir")
        print("2- ver quem é")
        ops = input()
        if ops == "1":
          print("Por onde você quer fugir?")
          print("1- janela")
          print("2- porta dos fundos")
          ops = input()
          if ops == "1":
            print("Quando você abriu a janela, descobriu que não era apenas um hacker mas sim 3")
            print("Você morreu")
            break
          else:
            if ops == "2":
              print("Você conseguiu escapar sem ninguem te ver, foi até a delegacia")
              print("Os policiais prenderam o hacker e te levaram para casa")
              tprint("Parabéns!!")
              print("Você conseguiu sobreviver")
        if ops == "2":
          print("Você foi até a porta viu que era o hacker porém antes de fugir ele te matou")
          print("Você morreu")
          break
  if assistir == "2":
    print("Você assistiu o filme, deitou-se na cama e dormiu")
    tprint("Parbéns!!")
    print("Você sobreviveu a um dia de vida e ganhou o jogo!")
  break
janela.mainloop()


