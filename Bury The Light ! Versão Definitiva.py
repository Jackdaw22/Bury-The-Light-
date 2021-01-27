#!/usr/bin/env python
# coding: utf-8

# In[9]:



from random import randint
import random
import abc
class save:   #Daqui para baixo são as funções de carregamento
  def __Save1(self):
    print("Salvando...")
    file=open('BuryTheLight_save.txt','w+')
    file.write(str(checkpoint))
    file.write("\n")  
    file.write(str(len(time)))
    file.write("\n")           
    for i in range(0,len(time)):
      file.write(time[i].nome)
      file.write("\n")
      file.write(time[i].classe)
      file.write("\n")
      file.write(str(time[i].vigor))
      file.write("\n")
      file.write(str(time[i].mana))
      file.write("\n")
      file.write(str(time[i].energia))
      file.write("\n")
      file.write(str(time[i].agilidade))
      file.write("\n")
      file.write(time[i].Habilidade1)
      file.write("\n")
      file.write(time[i].Habilidade2)
      file.write("\n")
      file.write(str(time[i].dano))
      file.write("\n")
      file.write(str(time[i].powerup))
      file.write("\n")
      file.write(str(time[i].defense))
      file.write("\n")
    file.write("1")  
    file.close()
def Carregamento():
  try:
    file=open('BuryTheLight_save.txt','r')
    global time
    checkpoint=file.readline().strip()
    time=[]
    contador=file.readline().strip()
    try:
      for i in range(0,int(contador)):
        name=file.readline().strip()
        time.append(name)
        time[i]=jogador(name,file.readline().strip(),int(file.readline().strip()),int(file.readline().strip()),int(file.readline().strip()),int(file.readline().strip()),file.readline().strip(),file.readline().strip(),int(file.readline().strip()),int(file.readline().strip()),int(file.readline().strip()))
    except:
        print("Não foi encontrado nenhum jogo salvo.")
        return main()
    if int(checkpoint)==1:
      return combate2()
    if int(checkpoint)==2:
      return combate3()  
    if int(checkpoint)==3:
      return combate4()
  except: 
    print("Não foi possível achar dados salvos!")
    return main()      
class inimigo(abc.ABC):   #Daqui para baixo temos as classes dos inimigos
  @abc.abstractmethod  
  def atacar(self, target):
    pass  
class inimigos_comuns(inimigo):
  def __init__(self,nome,vida,dano,acerto):
    self.nome=nome
    self.vida=vida
    self.dano=dano
    self.acerto=acerto  
  def atacar(self, target):
    self.target=target
    self.acerto=randint(1,10)
    if self.acerto!=1:
      if target.defense-self.dano<0:
        target.vigor=target.vigor+target.defense-self.dano
        print(self.nome+" causou "+str(self.dano-target.defense)+" de dano a "+target.nome+" que agora tem "+str(target.vigor)+" de vida restante")
        if target.defense!=0:
          print(target.nome+" teve sua defesa quebrada por "+self.nome)
          target.defense=target.defense-self.dano
          if target.defense<0:
            target.defense=0
      else:
        target.defense=target.defense-self.dano
        print(target.nome+" defendeu todo o dano de "+self.nome+", restando "+str(target.defense)+" de armadura")    
      if target.vigor<=0:
        print(target.nome+" está em estado CRÍTICO!!")
    else:
      acertador=randint(1,3)
      if acertador==1:
        print(self.nome+": Xii, errei!")
      if acertador==2:
        print(self.nome+": Mas que diabos, errei!")
      if acertador==3:
        print(self.nome+": Errei o golpe, só posso estar bêbado!") 
class inimigos_treinados(inimigo):
  def __init__(self,nome,vida,dano,acerto):
    self.nome=nome
    self.vida=vida
    self.dano=dano
    self.acerto=acerto  
  def habilidade(self):
    print(self.nome+": Rogo aos anjos que me curem!")
    self.vida=self.vida+5
    print(self.nome+" curou 5 pontos de vida")  
  def atacar(self, target):
    self.target=target
    self.acerto=randint(1,10)
    if self.acerto!=1:
      if target.defense-self.dano<0:
        target.vigor=target.vigor+target.defense-self.dano
        print(self.nome+" causou "+str(self.dano-target.defense)+" de dano a "+target.nome+" que agora tem "+str(target.vigor)+" de vida restante")
        if target.defense!=0:
          print(target.nome+" teve sua defesa quebrada por "+self.nome)
          target.defense=target.defense-self.dano
          if target.defense<0:
            target.defense=0
      else:
        target.defense=target.defense-self.dano
        print(target.nome+" defendeu todo o dano de "+self.nome+", restando "+str(target.defense)+" de armadura")    
      if target.vigor<=0:
        print(target.nome+" está em estado CRÍTICO!!")
    else:
      acertador=randint(1,3)
      if acertador==1:
        print(self.nome+": Droga, errei meu golpe!")
      if acertador==2:
        print(self.nome+": Te acertarei na próxima, patife!")
      if acertador==3:
        print(self.nome+": Maldito ser esguio!")    
class Knight_of_the_round(inimigo):
  def __init__(self,nome,vida,dano,acerto):
    self.nome=nome
    self.vida=vida
    self.dano=dano
    self.acerto=acerto  
  def habilidade(self):
    if self.nome=="Lander":
      print("Lander: Não vou deixar ninguém cair!")
      for i in range(0,len(time_inimigo)):
        time_inimigo[i].vida=time_inimigo[i].vida+15
      print("Lander cura 15 de vida de todos os aliados")
    if self.nome=="Draahl":
      print("Draahl: Pela glória do império órquico!")
      for i in range(0,len(time)):
        time[i].vigor=time[i].vigor-15
      print("Draahl causa 15 de dano verdadeiro em todos os adversários!")
    if self.nome=="Greg Morthos":
      alvo=randint(0,len(time)-1)
      while time[alvo].vigor==0:
        alvo=randint(0,len(time)-1)
      print("Morthos: Bahamut, abençoe minha lâmina, contra meus inimigos!")
      time[alvo].vigor=time[alvo].vigor-50
      print("Morthos causou 50 de dano verdadeiro a "+time[alvo].nome)
    if self.nome=="Kael":
      print("Kael: METEORO!!!!!!!!!!!!")
      for i in range(0,len(time)):
        time[i].vigor=time[i].vigor-30
        if time[i].vigor<=0:
          print(time[i].nome+" está em ESTADO CRÍTICO!!!")
      for i in range(0,len(time_inimigo)):
        time_inimigo[i].vida=time_inimigo[i].vida-30
        if time_inimigo[i].vida<=0:
          print(time_inimigo[i].nome+" foi esmagado por Kael!")  
    if self.nome=="Semper":
      skill=randint(1,2)
      if skill==1:
        print("Semper: SEJAM PROFANADOS! ATÉ OS OSSOS!")
        for i in range(0,len(time)):
          time[i].vigor=time[i].vigor-40
        print("Semper profana o solo ao redor do grupo, todos sofrem 40 de dano")
      if skill==2:
        print("Semper: VOU DRENAR ATÉ A ÚLTIMA GOTA DO SEU SANGUE!")
        for i in range(0,len(time)):
          time[i].mana=time[i].mana-20  
          time[i].energia=time[i].energia-20
          time[i].agilidade=time[i].agilidade-20
        print("Semper drena os recursos de todo o grupo!")  
  def atacar(self, target):
    self.target=target
    self.acerto=randint(1,10)
    if self.acerto!=1:
      if target.defense-self.dano<0:
        target.vigor=target.vigor+target.defense-self.dano
        print(self.nome+" causou "+str(self.dano-target.defense)+" de dano a "+target.nome+" que agora tem "+str(target.vigor)+" de vida restante")
        if target.defense!=0:
          print(target.nome+" teve sua defesa quebrada por "+self.nome)
          target.defense=target.defense-self.dano
          if target.defense<0:
            target.defense=0
      else:
        target.defense=target.defense-self.dano
        print(target.nome+" defendeu todo o dano de "+self.nome+", restando "+str(target.defense)+" de armadura")    
      if target.vigor<=0:
        print(target.nome+" está em estado CRÍTICO!!")
    else:
      acertador=randint(1,3)
      if acertador==1:
        print(self.nome+": Droga, errei meu golpe!")
      if acertador==2:
        print(self.nome+": O Vilão desviou!")
      if acertador==3:
        print(self.nome+": Não escapará do meu próximo golpe, vilão!!")                    
class personagem(abc.ABC): #Aqui é a base para os métodos dos personagens
  @abc.abstractmethod
  def descansar(self):
    pass
  @abc.abstractmethod
  def concentrar(self):
    pass  
#Daqui para baixo estão as classes disponíveis para os personagens predefinidos e a classe do jogador   
class mago(personagem):
  def __init__(self,nome,classe,vigor,mana,energia,agilidade,Habilidade1,Habilidade2,dano,powerup,defense):
    self.nome=nome
    self.classe=classe
    self.vigor=vigor
    self.mana=mana
    self.energia=energia
    self.agilidade=agilidade
    self.Habilidade1=Habilidade1
    self.Habilidade2=Habilidade2
    self.dano=dano
    self.powerup=powerup
    self.defense=defense
  def descansar(self):
    self.mana=self.mana+3  
  def concentrar(self):
    self.powerup=self.powerup+1  
class jogador(personagem):   #Essa é a base do personagem do jogador
  def __init__(self,nome,classe,vigor,mana,energia,agilidade,Habilidade1,Habilidade2,dano,powerup,defense):
    self.nome=nome
    self.classe=classe
    self.vigor=vigor
    self.mana=mana
    self.energia=energia
    self.agilidade=agilidade
    self.Habilidade1=Habilidade1
    self.Habilidade2=Habilidade2
    self.dano=dano
    self.powerup=powerup
    self.defense=defense
  def descansar(self):
    self.mana=self.mana+3
    self.energia=self.energia+3
    self.agilidade=self.agilidade+3
  def concentrar(self):
    self.powerup=self.powerup+1    
  def defender(self):
    self.defense=self.defense+self.energia  
class guerreiro(personagem):
  def __init__(self,nome,classe,vigor,mana,energia,agilidade,Habilidade1,Habilidade2,dano,powerup,defense):
    self.nome=nome
    self.classe=classe
    self.vigor=vigor
    self.mana=mana
    self.energia=energia
    self.agilidade=agilidade
    self.Habilidade1=Habilidade1
    self.Habilidade2=Habilidade2
    self.dano=dano
    self.powerup=powerup
    self.defense=defense
  def descansar(self):
    self.energia=self.energia+3
  def concentrar(self):
    self.powerup=self.powerup+1   
  def defender(self):
    self.defense=self.defense+self.energia   
class ladino(personagem):
  def __init__(self,nome,classe,vigor,mana,energia,agilidade,Habilidade1,Habilidade2,dano,powerup,defense):
    self.nome=nome
    self.classe=classe
    self.vigor=vigor
    self.mana=mana
    self.energia=energia
    self.agilidade=agilidade
    self.Habilidade1=Habilidade1
    self.Habilidade2=Habilidade2
    self.dano=dano
    self.powerup=powerup
    self.defense=defense
  def descansar(self):
    self.agilidade=self.agilidade+3
  def concentrar(self):
    self.powerup=self.powerup+1  
def confirmador(N,nome):  # Daqui para baixo tem as funções de confirmação/validação
  confirmado=False
  while confirmado!=True:
    try:
      z=int(nome)-1
      confirmado=True
    except:
      print("Entre um valor válido")
      nome=input()
      return confirmador(N,nome)
  if confirmado==True:
    if (int(nome)>=1 and int(nome)<=N):
      return int(nome)
    else:
      print("Entre um valor válido")
      nome=input()
      return confirmador(N,nome)     
def name_confirmator(nome):
  contador=0  
  for i in range(0,len(nome)):
   if nome[i]==" ":
    contador=contador+1
  if contador==len(nome):
    print("Você entrou algo inválido!")
    nome=input()
    return name_confirmator(nome)
  else:
    return nome
def main():       #Aqui é o menu inicial (Função de Menu)
  global eye
  eye=save()
  print("Bury The Light")
  print("1. Começar jogo")
  print("2. Sair do jogo")
  N=2
  comando=input() 
  auxiliador=confirmador(N,comando)
  if auxiliador==1:
    #Aqui começa o segundo menu (Menu de criação)
    print("1. Criar personagem (Você escolherá seu time logo em seguida)")
    print("2. Carregar jogo salvo")
    print("3. Retornar ao menu principal")
    comando=input()
    N=3
    auxiliador=confirmador(N,comando)
    if auxiliador==1:
      criador_de_personagem()
    if auxiliador==2:
      Carregamento()
    if auxiliador==3:
      return main()
  if auxiliador==2:
    #Encerra o jogo
    print("Obrigado por jogar")
    return 0
def criador_de_personagem():  #Aqui o personagem do jogador é criado
  global player
  Nome_do_player=input("Qual será o nome do seu personagem? ")
  Nome_do_player=name_confirmator(Nome_do_player)
  Classe_do_player=input("Qual será sua classe? ")
  Classe_do_player=name_confirmator(Classe_do_player)  
  print("Você tem 40 pontos para distribuir entre 4 status")
  confirmado = False
  while confirmado != True:
    try:
      Vigor_do_player=int(input("Quanto terá de vigor? "))
      Mana_do_player=int(input("Quanto terá de mana? "))
      Energia_do_player=int(input("Quanto terá de energia? "))
      Agilidade_do_player=int(input("Quanto terá de agilidade? "))
      confirmado=True
    except:
      print("Você enviou algum valor inválido, tente novamente")
  while Vigor_do_player+Mana_do_player+Energia_do_player+Agilidade_do_player>40 or Vigor_do_player+Mana_do_player+Energia_do_player+Agilidade_do_player<40 or Vigor_do_player<0 or  Mana_do_player<0 or Energia_do_player<0 or Agilidade_do_player<0:
    confirmado=True
    if Vigor_do_player+Mana_do_player+Energia_do_player+Agilidade_do_player>40:
      print("Você excedeu o limite de pontos para status, tente novamente")
    if Vigor_do_player+Mana_do_player+Energia_do_player+Agilidade_do_player<40:
      print("Você não colocou pontos suficientes, tente novamente")
    if Vigor_do_player<0 or  Mana_do_player<0 or Energia_do_player<0 or Agilidade_do_player<0:
      print("Entre apenas valores positivos!")  
    while confirmado!=False:  
      try:  
        Vigor_do_player=int(input("Quanto terá de vigor? "))
        Mana_do_player=int(input("Quanto terá de mana? "))
        Energia_do_player=int(input("Quanto terá de energia? "))
        Agilidade_do_player=int(input("Quanto terá de agilidade? "))
        
        confirmado=False
      except:
        print("Você entrou algum valor inválido, tente novamente")          
  Vigor_do_player=Vigor_do_player+5
  Mana_do_player=Mana_do_player+5
  Energia_do_player=Energia_do_player+5
  Agilidade_do_player=Agilidade_do_player+5
  dano_do_player=5    
  Contador_Habilidade1_do_player=0
  Contador_Habilidade2_do_player=0
  while Contador_Habilidade1_do_player==0:
    print("Escolha sua primeira habilidade")
    print("1. Prece de Cura")
    print("Um feitiço de cura rápida, que restaura 7 pontos de vida de todos os aliados, ao custo de 5 de mana")
    print("2. Ataque Viceral")
    print("Um ataque rápido que causa 5 de dano a todos os inimigos, ao custo de 5 de agilidade")
    print("3. Estocada")
    print("Um ataque direto em um único alvo, causando 10 de dano, ao custo de 5 de energia")
    print("4. Foco")
    print("Uma técnica de concentração dobrando o dano da próxima habilidade, ao custo de 5 de mana")
    N=4
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==1:
      Habilidade1_do_player="Prece de cura"
      Contador_Habilidade1_do_player=Contador_Habilidade1_do_player+1
    if auxiliador==2:
      Habilidade1_do_player="Ataque Viceral"
      Contador_Habilidade1_do_player=Contador_Habilidade1_do_player+1
    if auxiliador==3:
      Habilidade1_do_player="Estocada"
      Contador_Habilidade1_do_player=Contador_Habilidade1_do_player+1
    if auxiliador==4:
      Habilidade1_do_player="Foco"
      Contador_Habilidade1_do_player=Contador_Habilidade1_do_player+1  
  while Contador_Habilidade2_do_player==0:
    print("Escolha sua segunda habilidade")
    print("1. Disparo de fogo")
    print("Um poderoso disparo de fogo, que causa o equivalente a mana restante como dano em um único alvo, ao custo de 10 de mana")
    print("2. All in")
    print("Um terrível ataque sombrio, que causa o equivalente a agilidade restante como dano em um único alvo, caso o alvo morra o usuário ganha vigor e tem o custo da skill reduzido")
    print("3. Milagre")
    print("Uma prece desesperada, curando 15 de vida de todos os aliados, podendo trazer aliados em perigo de volta a vida, ao custo de 10 de mana")
    print("4. Proteger")
    print("Uma técnica defensiva, ganha o equivalente a energia restante como armadura, ao custo de 10 de energia")
    N=4
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==1:
      Habilidade2_do_player="Disparo de fogo"
      Contador_Habilidade2_do_player=Contador_Habilidade2_do_player+1
    if auxiliador==2:
      Habilidade2_do_player="All in"
      Contador_Habilidade2_do_player=Contador_Habilidade2_do_player+1
    if auxiliador==3:
      Habilidade2_do_player="Milagre"
      Contador_Habilidade2_do_player=Contador_Habilidade2_do_player+1
    if auxiliador==4:
      Habilidade2_do_player="Proteger"
      Contador_Habilidade2_do_player=Contador_Habilidade2_do_player+1  
  player=jogador(Nome_do_player,Classe_do_player,Vigor_do_player,Mana_do_player,Energia_do_player,Agilidade_do_player,Habilidade1_do_player,Habilidade2_do_player,dano_do_player,1,0)
  print("Seu nome é: "+player.nome + " Sua Classe é: "+player.classe+" Tem "+str(player.vigor)+" pontos de vida "+str(player.mana)+" pontos de mana "+str(player.energia)+" pontos de energia "+str(player.agilidade)+" pontos de agilidade")
  print("Suas habilidades são: "+player.Habilidade1+" e "+player.Habilidade2)
  print("Confirmar personagem?")
  print("1. Confirmar")
  print("2. Reeditar")
  comando=input()
  N=2
  auxiliador=confirmador(N,comando)
  if (auxiliador==2):
    criador_de_personagem()
  if (auxiliador==1):
    personagem_criado=0
    personagem_criado=personagem_criado+1
    print("Agora selecione sua equipe")
    seletor_de_equipe()
def seletor_de_equipe():   #Aqui o usuário escolhe sua equipe
  global time
  global Michkin
  global Rogojín
  global Ilyusha
  global Edwin
  global Howl
  global Strangelove
  global Filipóvna
  global Thriller
  time = []
  print("Selecione três companheiros:")
  Michkin=mago("Michkin","Curandeiro",9,16,3,2,"Prece de cura","Milagre",5,1,0)
  print("1. Nome: Michkin, Classe: Curandeiro, Habilidades: Prece de cura e Milagre")
  dentro_do_time1=0
  Rogojín=ladino("Rogojín","Patife",7,4,2,20,"Ataque Viceral","All in",7,1,0)
  print("2. Nome: Rogojín, Classe: Patife, Habilidades: Ataque Viceral e All in")
  dentro_do_time2=0
  Ilyusha=guerreiro("Ilyusha","Justiceiro",18,2,16,8,"Estocada","Proteger",7,1,0)
  print("3. Nome: Ilyusha, Classe: Justiceiro, Habilidades: Estocada e Proteger")
  dentro_do_time3=0
  Edwin=mago("Edwin","Mago",8,19,1,3,"Foco","Disparo de fogo",4,1,0)
  print("4. Nome: Edwin, Classe: Mago, Habilidades: Foco e Disparo de fogo")
  dentro_do_time4=0
  Howl=mago("Howl","Mágico",9,11,3,20,"Foco","All in",4,1,0)
  print("5. Nome: Howl, Classe: Mágico, Habilidades: Foco e All in")
  dentro_do_time5=0
  Strangelove=mago("Strangelove","Mago Vermelho",11,17,9,7,"Prece de cura","Disparo de fogo",7,1,0)
  print("6. Nome: Strangelove, Classe: Mago Vermelho, Habilidades: Prece de cura e Disparo de fogo")
  dentro_do_time6=0
  Filipóvna=ladino("Filipóvna","Esgrimista",11,9,5,13, "Prece de cura","All in",9,1,0)
  print("7. Nome: Filipóvna, Classe: Esgrimista, Habilidades: Prece de cura e All in")
  dentro_do_time7=0
  Thriller=guerreiro("Thriller","Zumbi",40,0,20,0,"Gemer","Encarar",2,1,0)
  print("8. Nome: Thriller, Classe: Zumbi, Habilidades: Gemer e Encarar")
  dentro_do_time8=0
  aux=0
  while aux<3: 
    comando=input()
    N=8
    auxiliador=confirmador(N,comando)
    if dentro_do_time1!=0 and auxiliador==1:
      print("Esse personagem já está no seu time!")
    if auxiliador==1 and dentro_do_time1==0:    #Aqui adiciona Michkin no time
      time.append(Michkin)
      dentro_do_time1=dentro_do_time1+1
      aux=aux+1
    if dentro_do_time2!=0 and auxiliador==2:
      print("Esse personagem já está no seu time!")    
    if auxiliador==2 and dentro_do_time2==0:    #Aqui adiciona Rogojín no time
      time.append(Rogojín)
      dentro_do_time2=dentro_do_time2+1
      aux=aux+1
    if auxiliador==3 and dentro_do_time3!=0:
      print("Esse personagem já está no seu time!")    
    if auxiliador==3 and dentro_do_time3==0:    #Aqui adiciona Ilyusha no time
      time.append(Ilyusha)
      dentro_do_time3=dentro_do_time3+1
      aux=aux+1  
    if auxiliador==4 and dentro_do_time4!=0:
      print("Esse personagem já está no seu time!")
    if auxiliador==4 and dentro_do_time4==0:   #Aqui adiciona Edwin no time
      time.append(Edwin)
      dentro_do_time4=dentro_do_time4+1
      aux=aux+1  
    if auxiliador==5 and dentro_do_time5!=0:
      print("Esse personagem já está no time!")
    if auxiliador==5 and dentro_do_time5==0:   #Aqui adiciona Howl no time
      time.append(Howl)
      dentro_do_time5=dentro_do_time5+1
      aux=aux+1
    if auxiliador==6 and dentro_do_time6!=0:
      print("Esse personagem já está no time!")
    if auxiliador==6 and dentro_do_time6==0:   #Aqui adiciona Strangelove no time
      time.append(Strangelove)
      dentro_do_time6=dentro_do_time6+1
      aux=aux+1
    if auxiliador==7 and dentro_do_time7!=0:
      print("Esse personagem já está no time!")
    if auxiliador==7 and dentro_do_time7==0:   #Aqui adiciona Filipóvna no time
      time.append(Filipóvna)
      dentro_do_time7=dentro_do_time7+1
      aux=aux+1  
    if auxiliador==8 and dentro_do_time8!=0:
      print("Esse personagem já está no time!")
    if auxiliador==8 and dentro_do_time8==0:   #Aqui adiciona Thriller no time
      time.append(Thriller)
      dentro_do_time8=dentro_do_time8+1
      aux=aux+1         
  print("Seu time é:")
  time.append(player)
  for i in range(len(time)):
    print(time[i].nome)      
  print("1. Confirmar")
  print("2. Exibir informações dos personagens")
  print("3. Refazer time")
  print("4. Refazer personagem")
  print("5. Voltar ao menu inicial")
  comando=input()
  N=5
  auxiliador=confirmador(N,comando)
  if auxiliador==1:
    print("Tudo pronto para iniciar o jogo")
    combate()
  if auxiliador==4:
    del time[0 : 2]
    time.pop(0)
    return criador_de_personagem() 
  if auxiliador==5:
    del time[0 : 2]
    time.pop(0)
    return main()
  if auxiliador==3:
    del time[0 : 2]
    time.pop(0)
    return seletor_de_equipe()
  if auxiliador==2:
    print("Seu nome é: "+player.nome + " Sua Classe é: "+player.classe+" Tem "+str(player.vigor)+" pontos de vida "+str(player.mana)+" pontos de mana "+str(player.energia)+" pontos de energia "+str(player.agilidade)+" pontos de agilidade")
    for i in range(0,3):
      print("Nome: "+time[i].nome+", Classe: "+time[i].classe+", Habilidades: "+time[i].Habilidade1+" e "+time[i].Habilidade2)
    print("1. Confirmar")
    print("2. Refazer time")
    print("3. Refazer personagem")
    print("4. Voltar ao menu principal")
    N=4
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==1:
      print("Tudo pronto para iniciar o jogo")
      combate()
    if auxiliador==3:
      del time[0 : 2]
      time.pop(0)
      return criador_de_personagem()  
    if auxiliador==4:
      del time[0 : 2]
      time.pop(0)
      return main()
    if auxiliador==2:
      return seletor_de_equipe() 
def habilidade1(pessoa):               #Daqui para baixo são as funções de habilidade
  if pessoa.Habilidade1=="Foco" and pessoa.mana>=5:
    pessoa.concentrar()
    pessoa.mana=pessoa.mana-5
    print(pessoa.nome+" está concentrada para um próximo ataque poderoso!")
  else:
    if pessoa.Habilidade1=="Foco" and pessoa.mana<5:
      print(pessoa.nome+" tentou usar Foco, mas não tem mana suficiente!")  
  if pessoa.Habilidade1=="Prece de cura" and pessoa.mana>=5:
    for i in range (0,len(time)):
      if time[i].vigor>0:
        time[i].vigor=time[i].vigor+7    
    print(pessoa.nome+" curou o grupo em 7 pontos de vida")
    pessoa.mana=pessoa.mana-5  
  else:
    if pessoa.Habilidade1=="Prece de cura" and pessoa.mana<5:
     print(pessoa.nome+" Tenta usar "+pessoa.Habilidade1+" mas falhou por não ter mana suficiente!")
  if pessoa.Habilidade1=="Ataque Viceral" and pessoa.agilidade>=5:
    for i in range (0,len(time_inimigo)):
      time_inimigo[i].vida=time_inimigo[i].vida-5*pessoa.powerup
    pessoa.agilidade=pessoa.agilidade-5    
    print("O ataque Viceral de "+pessoa.nome+" causou " +str(5*pessoa.powerup)+ " de dano a todo o time inimigo!!" ) 
    pessoa.powerup=1
  else:
    if pessoa.Habilidade1=="Ataque Viceral" and pessoa.agilidade<5:
      print(pessoa.nome+" tenta executar Ataque Viceral, mas não tem agilidade suficiente")    
  if pessoa.Habilidade1=="Estocada" and pessoa.energia>=5:
    alvo=randint(0,len(time_inimigo)-1)
    while time_inimigo[alvo].vida<=0:
      alvo=randint(0,len(time_inimigo)-1)
    time_inimigo[alvo].vida=time_inimigo[alvo].vida-10*pessoa.powerup
    pessoa.energia=pessoa.energia-5
    print(pessoa.nome+" causou "+str(10*pessoa.powerup)+" de dano a "+time_inimigo[alvo].nome+" que agora tem "+str(time_inimigo[alvo].vida)+" de vida restante")
    pessoa.powerup=1          
  else:
    if pessoa.Habilidade1=="Estocada" and pessoa.energia<5:
      print(pessoa.nome+" tentou usar Estocada mas falha por estar sem energia suficiente!!")
  if pessoa.Habilidade1=="Gemer":
    print(pessoa.nome+" geme de maneira ameaçadora")    
def habilidade2(pessoa):
  if pessoa.Habilidade2=="Disparo de fogo" and pessoa.mana>=10:
    alvo=randint(0,len(time_inimigo)-1)
    while time_inimigo[alvo].vida<=0:
      alvo=randint(0,len(time_inimigo)-1)
    time_inimigo[alvo].vida=time_inimigo[alvo].vida-pessoa.mana*pessoa.powerup
    print(pessoa.nome+" causou "+str(pessoa.mana*pessoa.powerup)+" de dano com disparo de fogo em "+time_inimigo[alvo].nome)
    pessoa.mana=pessoa.mana-10
    pessoa.powerup=1
  else:  
    if pessoa.Habilidade2=="Disparo de fogo" and pessoa.mana<10:
      print(pessoa.nome+" tenta usar Disparo de fogo, mas não tem mana suficiente!!")   
  if pessoa.Habilidade2=="Milagre" and pessoa.mana>=10:
    for i in range(0,len(time)):
      time[i].vigor=time[i].vigor+15
    pessoa.mana=pessoa.mana-10
    print(pessoa.nome+" curou o grupo todo em 15 pontos de vida!!")
  else:
    if pessoa.Habilidade2=="Milagre" and pessoa.mana<10:
      print(pessoa.nome+" tenta usar Milagre, mas não tem mana suficiente!") 
  if pessoa.Habilidade2=="All in" and pessoa.agilidade>=10:
    alvo=randint(0,len(time_inimigo)-1)
    while time_inimigo[alvo].vida<=0:
      alvo=randint(0,len(time_inimigo)-1)
    time_inimigo[alvo].vida=time_inimigo[alvo].vida-pessoa.agilidade*pessoa.powerup
    pessoa.powerup=1
    if time_inimigo[alvo].vida<=0:
      print(pessoa.nome+" matou "+time_inimigo[alvo].nome+" roubando "+str(pessoa.agilidade)+" pontos de vida!")
      pessoa.vigor=pessoa.vigor+pessoa.agilidade
      pessoa.agilidade=pessoa.agilidade-5
    else:
      print(pessoa.nome+" causou "+str(pessoa.agilidade*pessoa.powerup)+" de dano em "+time_inimigo[alvo].nome+", mas perdeu 10 pontos de vida")
      if pessoa.vigor<=0:
        print(pessoa.nome+" está em ESTADO CRÍTICO!")
      pessoa.vigor=pessoa.vigor-10
      pessoa.agilidade=pessoa.agilidade-10                   
  else:
    if pessoa.Habilidade2=="All in" and pessoa.agilidade<10:
      print(pessoa.nome+" tentou usar All in, mas não tem agilidade suficiente!!")
  if pessoa.Habilidade2=="Encarar":
    print(pessoa.nome+" encara o time inimigo!!")  
  if pessoa.Habilidade2=="Proteger" and pessoa.energia>=10:
    pessoa.defender()
    print(pessoa.nome+" reforçou sua armadura em "+str(pessoa.energia))
    pessoa.energia=pessoa.energia-10
  else:
    if pessoa.Habilidade2=="Proteger" and pessoa.energia<10:
      print(pessoa.nome+" tentou Proteger, mas não tem energia suficiente!!") 
    
def combate():             #daqui para baixo são as funções de jogo (Combate)
  random.shuffle(time)
  print("???: Ora, mas o que é isso? Já é São Valentim? Por que ainda estão aí deitados? (O grupo se levanta ainda um pouco atordoado)")
  print("1. O que está acontecendo?     2. Onde estamos?     3. Não me perturbe")
  N=3
  comando=input()
  auxiliador=confirmador(N,comando)
  if auxiliador==1 or auxiliador==2:
    print("Melquíades: Eu sou Melquíades, um necromante, e vocês são meus servos")
  if auxiliador==3:
    print("Melquíades: Não me dê ordens seu miserável! Eu sou Melquíades o grande")  
  print("Melquíades: Não tenho tempo para dispor com vocês, meros cadáveres inferiores")
  print("1. C-Cadáveres??     2. Acho que bebi demais ontem")
  N=2
  comando=input()
  auxiliador=confirmador(N,comando)
  if auxiliador==1:
    print("Melquíades: Sim! Cadáveres! Ressuscitei vocês temporariamente para uma tarefa")
  if auxiliador==2:
    print("Melquíades: Posso garantir que você não bebe nada a muito tempo! Ressuscitei vocês temporariamente para uma tarefa")
  print("Melquíades: Vou resumir, estão vendo aquela torre iluminada ali?")
  print("(Ele aponta para longe, onde uma torre de ouro se ergue no meio da mata densa)")
  print("Melquíades: Lá estão os 'Heróis', uns babacões diga-se de passagem, eles derrotaram as forças do mal e baniram a magia negra")
  print("1. Bom para eles     2. Vai demorar? Já estou ficando com fome")
  N=2
  comando=input()
  auxiliador=confirmador(N,comando)
  print("Melquíades: OLHE AQUI, ESTOU A UM PASSO DE TE MANDAR DE VOLTA PARA O TÚMULO")
  print("Melquíades: Matem os heróis e eu concedo uma ressureição verdadeira para cada um de vocês")
  print("(Melquíades se vira de repente antes de ir embora)")
  print("Melquíades: Antes que eu me esqueça, ressuscitei outros guerreiros caídos, imagino que eventualmente vocês vão trombar com outro grupo. ADEUS!") 
  print("\n")
  for i in range(0,len(time)):
    if time[i].nome=="Edwin":
      print("Edwin: Meu nome é Edwin (Vou cortar a cabeça deles assim que se virarem hihihi)")
      print("1. Oi?     2. Eu acabei de ouvir seu pensamento?")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Edwin: O-O que!? hmpf (Acho que pensei alto demais, maldição! Vou adiar meu ataque hihihi) eu sou do bem!")
    if time[i].nome=="Rogojín":
      print("Rogojín: Quero que todos fiquem cientes que não gosto de nenhum de vocês")
      print("1. Bem, pelo menos você foi sincero     2. Que dia maluco")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Rogojín: Nem tenta entrosar!")
    if time[i].nome=="Ilyusha":
      print("Ilyusha: Se trabalharmos juntos podemos vencer, tenho uma família que deve estar preocupada")
      print("1. Você parece uma pessoa descente     2. Finalmente um pouco de sanidade")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Ilyusha: Só quero acabar logo com isso")
    if time[i].nome=="Howl":
      print("Howl: Não há nada para se preocupar, eu vou sair dessa, EU VOU SAIR DESSA")
      print("1. Você parece preocupado     2. Você está com medo?")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Howl: AAAAAAAAAAAA como isso foi acontecer!?")
    if time[i].nome=="Strangelove":
      print("Strangelove: Os heróis de hoje não são como os de antigamente, hoje só são umas marícas, eu disse MARÍCAS")  
      print("1. Se você diz     2. Eu duvído")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Strangelove: Essa juventude nem respeita mais os soldados antigos")
    if time[i].nome=="Filipóvna":
      print("Filipóvna: Vocês já pararam para pensar que isso pode ser uma simulação computadorizada para um trabalho da faculdade de alguém?")
      print("1. hein?     2. Você bebeu?")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Filióvna: Deixa, não espero que vocês imbecis entendam")
    if time[i].nome=="Michkin":
      print("Michkín: Palavra que eu ainda estou sonhando, sonho uma ova, isso é um pesadelo")
      print("1. Encare a realidade     2. Seja homem")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Michkin: Não podia ter dito melhor!, vamos acabar com esse... Heróis... de uma figa")         
    if time[i].nome=="Thriller":
      print("Thriller: Arrrrrg hummmmp aahahah")
      print("1. Um zumbi?     2. O que diabos é você?")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      print("Thriller: Humfe wosdn")
  print("\n")    
  if time[0].nome!="Thriller":    
    print(time[0].nome+": Tem alguém vindo rapidamente, se preparem para o combate!")      
  else:
    print("Thriller: Humpf hampf homf (Tem bandidos vindo)")  
  print("1. Não escutei, pode repetir?     2. Que venham os miseráveis, vão sentir o gosto do meu poder")
  N=2
  comando=input()
  auxiliador=confirmador(N,comando)  
  print("Um grupo de bandidos aparece!!")
  global time_inimigo
  global bandido1
  global bandido2
  global bandidoChefe
  time_inimigo=[]
  bandido1=inimigos_comuns("Bandido 1",10,3,0)
  time_inimigo.append(bandido1)
  bandido2=inimigos_comuns("Bandido 2",10,2,0)
  time_inimigo.append(bandido2)
  bandidoChefe=inimigos_comuns("Bandido Chefe",15,5,0)
  time_inimigo.append(bandidoChefe)
  initiative=randint(1,2)
  contador_mortal_aliado=0
  contador_mortal_inimigo=0
  membros_aliados=len(time)
  membros_inimigos=3
  ordem_aliada=0
  ordem_inimiga=0
  vitória=0
  derrota=0
  while derrota==0 and vitória==0:
    if initiative==1:
      count1=0
      count=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1
      if time[ordem_aliada].vigor>0 and ordem_aliada!=len(time):
        print("================================")
        print("Vez de "+time[ordem_aliada].nome+ " Vida: "+str(time[ordem_aliada].vigor)+" Mana: "+str(time[ordem_aliada].mana)+" Energia: "+str(time[ordem_aliada].energia)+" Agilidade: "+str(time[ordem_aliada].agilidade))
        if time[ordem_aliada].defense>0:
            print("Armadura Acumulada: "+str(time[ordem_aliada].defense))
        for i in range(0,len(time_inimigo)):
          if time_inimigo[i].vida>0:
            print(time_inimigo[i].nome+" tem "+str(time_inimigo[i].vida)+" de vida restante")    
        print("1. Atacar")
        print("2. "+time[ordem_aliada].Habilidade1)
        print("3. "+time[ordem_aliada].Habilidade2)
        print("4. Descansar (Passar turno e recuperar energias)")
        print("================================")
        comando=input()
        N=4
        auxiliador=confirmador(N,comando)
        if auxiliador==1:
          target=randint(0,len(time_inimigo)-1)
          while time_inimigo[target].vida<=0:
            target=randint(0,len(time_inimigo)-1)
          dano=randint(1,time[ordem_aliada].dano)
          time_inimigo[target].vida=time_inimigo[target].vida-dano
          print(time[ordem_aliada].nome+" Causou " +str(dano)+ " de dano a "+time_inimigo[target].nome+" que agora tem "+str(time_inimigo[target].vida)+" de vida restante")
          if time_inimigo[target].vida<=0:
            contador_mortal_inimigo=contador_mortal_inimigo+1 
        if auxiliador==2:
          habilidade1(time[ordem_aliada])
        if auxiliador==3:
          habilidade2(time[ordem_aliada])
        if auxiliador==4:
          time[ordem_aliada].descansar()         
        ordem_aliada=ordem_aliada+1
        initiative=2
      else:
        if time[ordem_aliada].vigor<=0 and ordem_aliada!=len(time):
          ordem_aliada+1
          time.remove(time[ordem_aliada])
          initiative=2  
      if ordem_aliada>=len(time):
        ordem_aliada=0
        initiative=2 
    if initiative==2:
      count=0
      count1=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0: 
        vitória=vitória+1
      if derrota==0:  
        try:
          target=randint(0,len(time)-1)
          while time[target].vigor<=0:
            target=randint(0,len(time)-1)
        except:
          print("Você perdeu!")
        if time_inimigo[ordem_inimiga].vida>0 and ordem_inimiga!=len(time_inimigo):
          time_inimigo[ordem_inimiga].atacar(time[target])
          if time[target].vigor<=0:
            contador_mortal_aliado=contador_mortal_aliado+1
          ordem_inimiga=ordem_inimiga+1
          initiative=1
        else:
          if time_inimigo[ordem_inimiga].vida<=0 and ordem_inimiga!=len(time_inimigo):
            time_inimigo.remove(time_inimigo[ordem_inimiga])
            ordem_inimiga=ordem_inimiga+1
            initiative=1  
        if ordem_inimiga>=len(time_inimigo):
          initiative=1
          ordem_inimiga=0  
  if derrota!=0:
    print("Você perdeu!")
    return main()
  if vitória!=0:
    print("Você venceu")
    if time[0].nome!="Thriller":
      print(time[0].nome+": Hey até que somos bons, vamos seguir em frente")
    else:
      print("Thriller: humpf arrrg hoo (Muito bem, vamos seguir adiante")
    print("1. Vamos lá!     2. Eu sou incrível!")
    print("\n")
    N=2
    comando=input()
    auxiliador=confirmador(N,comando)
    print("Deseja salvar seu progresso?")
    print("1. Sim     2. Não")
    N=2
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==2:
      pass
    if auxiliador==1:
      global checkpoint
      checkpoint=1
      eye._save__Save1()  
    return combate2()          
def combate2():
  global time_inimigo
  global PatrulhaDaTorre1
  global PatrulhaDaTorre2
  global ChefeDaPatrulha
  print("O grupo anda por algum tempo até chegar aos arredores da torre, a floresta estava repleta de restos de batalha")
  print("Algum outro grupo já havia passado por ali, a julgar pelos corpos e armas atiradas ao chão do bosque")
  print("De repente uma movimentação estranha faz todos ficarem alerta, três soldados patrulhavam os arredores em busca de inimigos")
  print("Chefe da Patrulha: Alto! Quem são vocês!? (Ele diz desembainhando a espada)")
  if time[0].nome!="Thriller":
    print(time[0].nome+(": Acho que vamos para outra batalha!"))
  else:
    print("Thriller: Humpf hompf bobg (Lá vamos nós mais uma vez)")  
  print("\n")  
  time_inimigo=[]
  PatrulhaDaTorre1=inimigos_treinados("Patrulha da Torre",15,5,0)
  time_inimigo.append(PatrulhaDaTorre1)
  PatrulhaDaTorre2=inimigos_treinados("Patrulha da Torre",15,5,0)
  time_inimigo.append(PatrulhaDaTorre2)
  ChefeDaPatrulha=inimigos_treinados("Chefe da Patrulha",20,8,0)
  time_inimigo.append(ChefeDaPatrulha)
  initiative=randint(1,2)
  contador_mortal_aliado=0
  contador_mortal_inimigo=0
  membros_aliados=len(time)
  membros_inimigos=3
  ordem_aliada=0
  ordem_inimiga=0
  vitória=0
  derrota=0
  while vitória==0 and derrota==0:
    if initiative==1:
      count1=0
      count=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1  
      if time[ordem_aliada].vigor>0 and ordem_aliada!=len(time):
        print("================================")
        print("Vez de "+time[ordem_aliada].nome+ " Vida: "+str(time[ordem_aliada].vigor)+" Mana: "+str(time[ordem_aliada].mana)+" Energia: "+str(time[ordem_aliada].energia)+" Agilidade: "+str(time[ordem_aliada].agilidade))
        if time[ordem_aliada].defense>0:
            print("Armadura Acumulada: "+str(time[ordem_aliada].defense))
        for i in range(0,len(time_inimigo)):
          if time_inimigo[i].vida>0:
            print(time_inimigo[i].nome+" tem "+str(time_inimigo[i].vida)+" de vida restante")    
        print("1. Atacar")
        print("2. "+time[ordem_aliada].Habilidade1)
        print("3. "+time[ordem_aliada].Habilidade2)
        print("4. Descansar (Passar turno e recuperar energias)")
        print("================================")
        comando=input()
        N=4
        auxiliador=confirmador(N,comando)
        if auxiliador==1:
          target=randint(0,len(time_inimigo)-1)
          while time_inimigo[target].vida<=0:
            target=randint(0,len(time_inimigo)-1)
          dano=randint(1,time[ordem_aliada].dano)
          time_inimigo[target].vida=time_inimigo[target].vida-dano
          print(time[ordem_aliada].nome+" Causou " +str(dano)+ " de dano a "+time_inimigo[target].nome+" que agora tem "+str(time_inimigo[target].vida)+" de vida restante")
          if time_inimigo[target].vida<=0:
            contador_mortal_inimigo=contador_mortal_inimigo+1
        if auxiliador==2:
          habilidade1(time[ordem_aliada])
        if auxiliador==3:
          habilidade2(time[ordem_aliada])
        if auxiliador==4:
          time[ordem_aliada].descansar()         
        ordem_aliada=ordem_aliada+1
        initiative=2
      else:
        if time[ordem_aliada].vigor<=0 and ordem_aliada!=len(time):
          ordem_aliada+1
          time.remove(time[ordem_aliada])
          initiative=2  
      if ordem_aliada>=len(time):
        ordem_aliada=0
        initiative=2 
    if initiative==2:
      count=0
      count1=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1        
      try:
        target=randint(0,len(time)-1)
      except:
        pass
      if derrota==0:  
        while time[target].vigor<=0:
          target=randint(0,len(time)-1)  
        if time_inimigo[ordem_inimiga].vida>0 and ordem_inimiga!=len(time_inimigo):
          action=randint(1,4)
          if action==1 or action==3 or action==4:
            time_inimigo[ordem_inimiga].atacar(time[target])
          if action==2:
            time_inimigo[ordem_inimiga].habilidade()  
          if time[target].vigor<=0:
            contador_mortal_aliado=contador_mortal_aliado+1
          ordem_inimiga=ordem_inimiga+1
          initiative=1
        else:
          if time_inimigo[ordem_inimiga].vida<=0 and ordem_inimiga!=len(time_inimigo):
            time_inimigo.remove(time_inimigo[ordem_inimiga])
            ordem_inimiga=ordem_inimiga+1
            initiative=1  
        if ordem_inimiga>=len(time_inimigo):
          initiative=1
          ordem_inimiga=0 
  if derrota!=0:
    print("Você perdeu!")
    return main()
  if vitória!=0:
    print("A equipe conseguiu vencer facilmente o grupo de patrulheiros, o caminho para a entrada da torre estava livre.")
    print("Deseja salvar seu progresso?")
    print("1. Sim     2. Não")
    N=2
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==2:
      pass
    if auxiliador==1:
      global checkpoint
      checkpoint=2
      eye._save__Save1()
    return combate3()
def combate3():
  global time_inimigo
  global Semper
  global GregMorthos
  global Lander
  global Kael
  global Draahl
  print("\n")
  print("O grupo chega ao salão principal, passando pelo pátio da torre, o cheiro fétido dos cadáveres deixava claro que algum outro grupo havia passado por ali")
  print("Tudo foi esclarecido ao chegarem no salão dos heróis, um grupo de fato havia passado por lá, mas seus cadáveres atirados ao chão mostrava o insucesso deles perante aos heróis")
  print("Estes por sua vez estavam reunidos, fadigados da batalha. Todos olham imediatamente para o grupo que entrou no local")
  print("Lander: *ofegante* Pela graça dos anjos e da luz, esses cadáveres revividos não param de aparecer, por sorte minha Holy Avenger ainda tem sede de sangue infiel (Ele olha para a espada)")
  print("Morthos: Isso é um sinal que forças do mal ainda habitam este continente, mas digam-me caros cadáveres, é mesmo a vileza que os motiva?")
  print("1. Claro que não, um mago do mal nos trouxe de volta e nos obrigou a vir aqui     2. Sim, nós somos vís, não teremos piedade de vocês")
  N=2
  comando=input()
  auxiliador=confirmador(N,comando)
  if auxiliador==1:
    print("Draahl: Podemos resolver isso diplomaticamente então companheiros, vejam bem, queremos ajuda-los a sair desse sufoco.")
    print("Semper: Não seja tolo, Draahl, eles são aliados das forças sombrias, precisam ser derrotados")
    print("Lander: Odeio admitir mas concordo com nosso necromante, querendo ou não eles são aliados das forças sombrias") 
  if auxiliador==2:
    print("Kael: Estão vendo caros colegas? Eles não tem nem um pingo de inteligência e precisam ser EXTERMINADOS")
    print("Lander: Tudo isso está muito estranho, Semper, por que está tão calado?")
    print("Semper: Estou tão surpreso quanto vocês, mas temos que tomar uma providência logo, eles são perigosos")  
  print("Morthos: Basta, Semper, tem certeza que não consegue quebrar o feitiço e manda-los de volta ao além?")
  print("Semper: Já disse que um necromante não pode interferir no feitiço de outro, qualquer coisa que eu faça pode acabar até ajudando eles")
  print("\n")
  print("(A voz de Melquíades ressoa em sua mente)")
  print("Melquíades: Vejo que chegaram ao destino final, Vou ser sincero, vocês não tem a menor chance, mas vou dar um pouco do meu poder")
  print("(Você sente uma infusão de poder)")
  for i in range(0,len(time)):
    time[i].vigor=time[i].vigor+60
    time[i].mana=time[i].mana+40
    time[i].energia=time[i].energia+40
    time[i].agilidade=time[i].agilidade+40 
    time[i].dano=time[i].dano*2 
  time_inimigo=[]
  GregMorthos=Knight_of_the_round("Greg Morthos",65,25,0)
  time_inimigo.append(GregMorthos)
  Lander=Knight_of_the_round("Lander",80,15,0)
  time_inimigo.append(Lander)
  Kael=Knight_of_the_round("Kael",50,10,0)
  time_inimigo.append(Kael)
  Draahl=Knight_of_the_round("Draahl",70,20,0)
  time_inimigo.append(Draahl)
  initiative=randint(1,2)
  contador_mortal_aliado=0
  contador_mortal_inimigo=0
  membros_aliados=len(time)
  membros_inimigos=3
  ordem_aliada=0
  ordem_inimiga=0
  vitória=0
  derrota=0
  while vitória==0 and derrota==0:
    if initiative==1:
      count1=0
      count=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1  
      if vitória==0 and derrota==0:  
        if time[ordem_aliada].vigor>0 and ordem_aliada!=len(time):
          print("================================")
          print("Vez de "+time[ordem_aliada].nome+ " Vida: "+str(time[ordem_aliada].vigor)+" Mana: "+str(time[ordem_aliada].mana)+" Energia: "+str(time[ordem_aliada].energia)+" Agilidade: "+str(time[ordem_aliada].agilidade))
          if time[ordem_aliada].defense>0:
            print("Armadura Acumulada: "+str(time[ordem_aliada].defense))
          for i in range(0,len(time_inimigo)):
            if time_inimigo[i].vida>0:
              print(time_inimigo[i].nome+" tem "+str(time_inimigo[i].vida)+" de vida restante")    
          print("1. Atacar")
          print("2. "+time[ordem_aliada].Habilidade1)
          print("3. "+time[ordem_aliada].Habilidade2)
          print("4. Descansar (Passar turno e recuperar energias)")
          print("================================")
          comando=input()
          N=4
          auxiliador=confirmador(N,comando)
          if auxiliador==1:
            target=randint(0,len(time_inimigo)-1)
            while time_inimigo[target].vida<=0:
              target=randint(0,len(time_inimigo)-1)
            dano=randint(1,time[ordem_aliada].dano)
            time_inimigo[target].vida=time_inimigo[target].vida-dano
            print(time[ordem_aliada].nome+" Causou " +str(dano)+ " de dano a "+time_inimigo[target].nome+" que agora tem "+str(time_inimigo[target].vida)+" de vida restante")
            if time_inimigo[target].vida<=0:
              contador_mortal_inimigo=contador_mortal_inimigo+1
          if auxiliador==2:
            habilidade1(time[ordem_aliada])
          if auxiliador==3:
            habilidade2(time[ordem_aliada])
          if auxiliador==4:
            time[ordem_aliada].descansar()         
          ordem_aliada=ordem_aliada+1
          initiative=2
        else:
          if time[ordem_aliada].vigor<=0 and ordem_aliada!=len(time):
            ordem_aliada+1
            time.remove(time[ordem_aliada])
            initiative=2  
        if ordem_aliada>=len(time):
          ordem_aliada=0
          initiative=2 
    if initiative==2:
      count=0
      count1=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1        
      try:
        target=randint(0,len(time)-1)
      except:
        pass
      if derrota==0 and vitória==0:  
        while time[target].vigor<=0:
          target=randint(0,len(time)-1)  
        if time_inimigo[ordem_inimiga].vida>0 and ordem_inimiga!=len(time_inimigo):
          action=randint(1,4)
          if action==1 or action==3 or action==4:
            time_inimigo[ordem_inimiga].atacar(time[target])
          if action==2:
            time_inimigo[ordem_inimiga].habilidade()  
          if time[target].vigor<=0:
            contador_mortal_aliado=contador_mortal_aliado+1
          ordem_inimiga=ordem_inimiga+1
          initiative=1
        else:
          if time_inimigo[ordem_inimiga].vida<=0 and ordem_inimiga!=len(time_inimigo):
            time_inimigo.remove(time_inimigo[ordem_inimiga])
            ordem_inimiga=ordem_inimiga+1
            initiative=1  
        if ordem_inimiga>=len(time_inimigo):
          initiative=1
          ordem_inimiga=0 
  if derrota!=0:
    print("Você perdeu!")
    return main()
  if vitória!=0:
    print("\n")
    print("Morthos: M-mas o que é isso? Semper... não vai lutar?")
    print("Semper: *sorrindo* finalmente, meu caminho para grandeza está livre!")
    print("Semper: Fizeram muito bem meus lacaios, agora podem viver novamente (Ele lança um feitiço)")
    print("(Todos se sentem vivos de novo)")
    print("1. Eu não estou entendendo nada     2. Mas hein!?")
    N=2
    comando=input()
    auxiliador=confirmador(N,comando)
    print("Semper: Entreguei a ressureição verdadeira que havia prometido, não me decepcione, não desvendaram ainda que eu era Melquíades?")
    print("Semper: Estava esperando o momento que esses vermes iam se acomodar, sem suas forças de outrora, nenhum deles tinha chance contra minha legião de mortos vivos")
    print("Semper: Meu plano de dominação se inicia agora *Sorri* O que estão esperando podem ir embora, não tenho mais uso para vocês")
    print("1. Não vou te deixar sair impune, patife!     2. Sendo assim vou para casa, adeus")
    N=2
    comando=input()
    auxiliador=confirmador(N,comando)
    if auxiliador==2:
      print("Você finalizou o jogo! Ainda que com o final ruim, parabéns da mesma forma!")
      return main()
    if auxiliador==1:
      print("Deseja salvar seu progresso?")
      print("1. Sim     2. Não")
      N=2
      comando=input()
      auxiliador=confirmador(N,comando)
      if auxiliador==2:
        pass
      if auxiliador==1:
        global checkpoint
        checkpoint=3
        eye._save__Save1()
      combate4()  
def combate4():
  global time_inimigo
  global Semper  
  print("Semper: Meus próprios servos, me ameaçando?")
  print("Semper: Vocês são muito burros mesmo! Olhe o tanto de cadáveres por aqui, nesse terreno eu sou quase um DEUS!")
  print("(O necromante lança um feitiço, retirando a força dos cadáveres e infundindo-a nele mesmo)")
  print("\n")  
  print("Semper: Destrui-los será um prazer!")
  time_inimigo=[]
  Semper=Knight_of_the_round("Semper",150,50,0)
  time_inimigo.append(Semper)
  initiative=randint(1,2)
  contador_mortal_aliado=0
  contador_mortal_inimigo=0
  membros_aliados=len(time)
  membros_inimigos=3
  ordem_aliada=0
  ordem_inimiga=0
  vitória=0
  derrota=0
  while vitória==0 and derrota==0:
    if initiative==1:
      count1=0
      count=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1  
      if time[ordem_aliada].vigor>0 and ordem_aliada!=len(time):
        print("================================")
        print("Vez de "+time[ordem_aliada].nome+ " Vida: "+str(time[ordem_aliada].vigor)+" Mana: "+str(time[ordem_aliada].mana)+" Energia: "+str(time[ordem_aliada].energia)+" Agilidade: "+str(time[ordem_aliada].agilidade))
        if time[ordem_aliada].defense>0:
            print("Armadura Acumulada: "+str(time[ordem_aliada].defense))
        for i in range(0,len(time_inimigo)):
          if time_inimigo[i].vida>0:
            print(time_inimigo[i].nome+" tem "+str(time_inimigo[i].vida)+" de vida restante")    
        print("1. Atacar")
        print("2. "+time[ordem_aliada].Habilidade1)
        print("3. "+time[ordem_aliada].Habilidade2)
        print("4. Descansar (Passar turno e recuperar energias)")
        print("================================")
        comando=input()
        N=4
        auxiliador=confirmador(N,comando)
        if auxiliador==1:
          target=randint(0,len(time_inimigo)-1)
          while time_inimigo[target].vida<=0:
            target=randint(0,len(time_inimigo)-1)
          dano=randint(1,time[ordem_aliada].dano)
          time_inimigo[target].vida=time_inimigo[target].vida-dano
          print(time[ordem_aliada].nome+" Causou " +str(dano)+ " de dano a "+time_inimigo[target].nome+" que agora tem "+str(time_inimigo[target].vida)+" de vida restante")
          if time_inimigo[target].vida<=0:
            contador_mortal_inimigo=contador_mortal_inimigo+1
        if auxiliador==2:
          habilidade1(time[ordem_aliada])
        if auxiliador==3:
          habilidade2(time[ordem_aliada])
        if auxiliador==4:
          time[ordem_aliada].descansar()         
        ordem_aliada=ordem_aliada+1
        initiative=2
      else:
        if time[ordem_aliada].vigor<=0 and ordem_aliada!=len(time):
          ordem_aliada+1
          time.remove(time[ordem_aliada])
          initiative=2  
      if ordem_aliada>=len(time):
        ordem_aliada=0
        initiative=2 
    if initiative==2:
      count=0
      count1=0
      for i in range(0,len(time)):
        if time[i].vigor>0:
          count=count+time[i].vigor
      if count==0:
        derrota=derrota+1
      for i in range(0,len(time_inimigo)):
        if time_inimigo[i].vida>0:
          count1=count1+time_inimigo[i].vida
      if count1==0:
        vitória=vitória+1        
      try:
        target=randint(0,len(time)-1)
      except:
        pass
      if derrota==0:  
        while time[target].vigor<=0:
          target=randint(0,len(time)-1)  
        if time_inimigo[ordem_inimiga].vida>0 and ordem_inimiga!=len(time_inimigo):
          action=randint(1,4)
          if action==1 or action==3 or action==4:
            time_inimigo[ordem_inimiga].atacar(time[target])
          if action==2:
            time_inimigo[ordem_inimiga].habilidade()  
          if time[target].vigor<=0:
            contador_mortal_aliado=contador_mortal_aliado+1
          ordem_inimiga=ordem_inimiga+1
          initiative=1
        else:
          if time_inimigo[ordem_inimiga].vida<=0 and ordem_inimiga!=len(time_inimigo):
            time_inimigo.remove(time_inimigo[ordem_inimiga])
            ordem_inimiga=ordem_inimiga+1
            initiative=1  
        if ordem_inimiga>=len(time_inimigo):
          initiative=1
          ordem_inimiga=0 
  if derrota!=0:
    print("Você perdeu!")
    return main()
  if vitória!=0:
    print("Com o Necromante derrotado, o grupo não viu mais razão para se manter unido, todos haviam vivido em locais diferente e em épocas diferentes.")
    print("Os heróis foram derrotados, mas o triunfo do mal foi rechaçado por um grupo unusual.")
    print("Você venceu, obrigado por jogar.")
    return main()           
 

if __name__=="__main__":
  main()  


# In[ ]:




