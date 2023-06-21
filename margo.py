from chatterbot import ChatBot
from chatBot import Bot
from chatterbot.trainers import ListTrainer
from baseDados import PerguntasAleatorias
from baseDados import Saudacoes
from baseDados import Eventos

# C:\Users\pauli\AppData\Local\Programs\Python\Python36\Lib\site-packages\chatterbot


class Margo:
  
  nomeBot = "Margo"
  
  def __init__(self):
    self.chat = Bot(self.nomeBot)

    #self.adicionarTreinos()

    self.introducao()
    
    self.nomeUsuario = self.olaMundo()
    
    self.iniciar()
    
  def introducao(self):
    print("========================================================================================")
    print("Python version: 3.6.7")
    print("ChatterBot version: 1.0.4")
    
    print("================================= MARGO CHAT =======================================================")
    print("Bem-vindo ao Chat com a ", self.nomeBot ," especialista em Planejamento de Eventos!")
    print("Este chatbot foi desenvolvido por alunas de uma universidade como parte de um trabalho da disciplina de Introdução à Inteligência Artificial, com foco em uso educacional. Nossa intenção é criar uma ferramenta interativa que possa auxiliá-lo no planejamento e organização de eventos, fornecendo informações, dicas e sugestões úteis.")
    print("Este chatbot é projetado para lidar com uma variedade de tópicos relacionados a eventos, como logística, orçamento, divulgação, seleção de local, entre outros. Ele está equipado com um conjunto de respostas pré-programadas e utiliza técnicas de processamento de linguagem natural para entender suas perguntas e fornecer respostas relevantes.")
    print("Nosso objetivo é tornar o planejamento de eventos uma tarefa mais fácil e acessível para você. Seja você um estudante, um organizador de eventos ou simplesmente alguém interessado em aprender mais sobre o assunto, estamos aqui para ajudar. Sinta-se à vontade para fazer suas perguntas e explorar as funcionalidades do chatbot.")
    print("Lembramos que este chatbot é um projeto em desenvolvimento e pode ter várias limitações.")
    print("Aproveite sua interação com o Chatbot de Planejamento de Eventos e desejamos sucesso em seus projetos de organização de eventos!")
    print("========================================================================================")
  
  def olaMundo(self):
    print("Margo: Olá, me chamo Margo, qual seu nome?")
    nome = input("Anônimo: ")
    print("Margo: Prazer em te conhecer "+ nome + ", tem alguma dúvida sobre eventos? ")
    return nome
    
    
  def adicionarTreinos(self):
    
    self.chat.trainer = ListTrainer(self.chat.chat)
    for treino in Saudacoes:
      self.chat.trainer.train(treino)
    for treino in Eventos:
      self.chat.trainer.train(treino)
    for treino in PerguntasAleatorias:
      self.chat.trainer.train(treino)
      
  def iniciar(self):
    
    while True: 
      pergunta = input(self.nomeUsuario + ": ").lower()
      texto = ""
      resposta = self.chat.chat.get_response(pergunta)
      if(resposta.confidence <= 0.5): texto = self.nomeBot + ": Tenho cerca de " + str(resposta.confidence * 100) + "% de certeza sobre esse assunto, talvez se formular sua mensagem de outra forma fica mais fácil, mesmo assim aqui vai minha resposta: "
      elif(resposta.confidence <= 0.7): texto = self.nomeBot + ": Tenho " + str(resposta.confidence * 100) + "% de certeza sobre esse assunto, então minha resposta pode estar errada mas aqui vai minha resposta: "
      elif(resposta.confidence <= 1): texto = self.nomeBot + ": Tenho " + str(resposta.confidence * 100) + "% de certeza sobre esse assunto, então minha resposta tem grandes chances de ser correta, aqui vai minha resposta: "
      
      print("")
      print(texto)
      
      print("")
      print(resposta)
      print("")
  

Margo()