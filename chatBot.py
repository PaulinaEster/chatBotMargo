from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from h2 import database
# from baseDados import baseDados

# caminho_banco_dados = "./db"
# conn = database.connect(caminho_banco_dados)
class Bot:
  
  baseDados = []
  
  def __init__(self, nome):
    self.chat = ChatBot(nome,
      logic_adapters = [
        "chatterbot.logic.BestMatch",
      ],
      preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'  
      ]
    )
    self.trainer = ListTrainer(self.chat)



# trainer.train(baseTreino)

# trainer.train("chatterbot.corpus.Portuguese.greetings")
# trainer.train("chatterbot.corpus.Portuguese.conversations")


# print("Margo: Olá, me chamo Margo, qual seu nome?")
# nome = input("Anônimo: ")
# print("Margo: Prazer em te conhecer "+ nome + ", tem alguma dúvida sobre eventos? ")

# def esmiucarPergunta(pergunta):
#   return pergunta.split(' ')

# def verificaPalavraNaoComum(palavra):
#   palavrasComuns = ['qual', 'quais', 'são', 'como', 'em', 'sobre']
#   if(palavra in palavrasComuns):
#     return True
#   return False  

# while True:
#   try:
#     pergunta = input(nome + ": ").lower()
    
#     resposta = chatbot.get_response(pergunta)
#     print(resposta.confidence)
    
#     # while(resposta.confidence <= 0):
#     #   for pesquisaBase in baseDados:
#     #     for palavraAssunto in esmiucarPergunta(pergunta):
#     #       if( verificaPalavraNaoComum(palavraAssunto) and palavraAssunto in pesquisaBase):
#     #         resposta = pesquisaBase
#     #   resposta = chatbot.get_response(pergunta)
#     #   print(resposta.confidence)
#     # if float(resposta.confidence) > 0:
#     print("Margo: ", resposta)
#     # else:
#     #   print("Desculpe, eu não vou conseguir tirar essa dúvida, mas você pode tentar escrever de uma forma diferente, quem sabe eu entenda!")
#   except(KeyboardInterrupt, EOFError, SystemExit):
#     break
  
  
