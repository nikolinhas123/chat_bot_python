
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import time

time.clock = time.time

bot = ChatBot('ChatBot')
bot.storage.drop()

perguntas = [
    "Qual é a capital da França?",
    "Quem escreveu 'Dom Quixote'?",
    "Qual é o maior planeta do Sistema Solar?",
    "Quem pintou a Mona Lisa?",
    "Qual é a cor do céu durante o dia?",
    "Quantos lados tem um triângulo?",
    "Quem foi o primeiro presidente dos Estados Unidos?",
    "Qual é o maior oceano do mundo?",
    "Qual é a fórmula química da água?",
    "Quem escreveu 'Harry Potter'?",
    "Quem descobriu a gravidade?",
    "Qual é o símbolo químico do ouro?",
    "Quem foi o primeiro homem a pisar na Lua?",
    "Qual é o país mais populoso do mundo?",
    "Quem foi o pintor do teto da Capela Sistina?",
    "Quantos elementos químicos existem na tabela periódica?",
    "Quem foi o criador da teoria da relatividade?",
    "Qual é a língua oficial do Brasil?",
    "Quem escreveu 'A Origem das Espécies'?",
    "Quem é conhecido como o 'Pai da Computação'?"
    "qual o professor mais legal"
]
    
respostas = [
    "Paris",
    "Miguel de Cervantes",
    "Júpiter",
    "Leonardo da Vinci",
    "Azul",
    "Três",
    "George Washington",
    "Oceano Pacífico",
    "H2O",
    "J.K. Rowling",
    "Isaac Newton",
    "Au",
    "Neil Armstrong",
    "China",
    "Michelangelo",
    "118",
    "Albert Einstein",
    "Português",
    "Charles Darwin",
    "Alan Turing",
    "yan carlos"
]

base_treino_teste = []
for i in range (len(perguntas)):
    base_treino_teste.append(perguntas[i])
    base_treino_teste.append(respostas[i])


trainer = ListTrainer(bot)
trainer.train(conversa)
#pergunta = ###Texto da interface do usuario
#resposta = bot.get_response(pergunta)


#taxa_acerto = resposta.confidence*100



janela = Tk()
janela.geometry("500x450+540+0")

txt = Text(height=10, width=61, background="darkgreen")
txt.grid(row=0,column=0)
txt.configure(state=DISABLED)

txt_send = Text(height=3, width=61, background="white")
txt_send.grid(row=2,column=0)

btn_send = Button(height=2, width=61, background="white", text="Enviar", fg="blue", command= lambda : enviar())
btn_send.grid(row=3,column=0)

#a1 = Button(text=" ", height=2, width=4, background="white")
#a1.place(x=10,y=60)

def enviar():
    txt.configure(state=NORMAL)
    txt.insert(END,"Eu disse: " + txt_send.get('1.0',END))
    pergunta = txt.send.get('1.0',END)
    txt_send.delete('1.0',END)
    txt.configure(state=DISABLED)
    resposta()

def resposta():
    txt.configure(state=NORMAL)
    txt.insert(END,"CHAT-BOT Disse: " + str(bot.get_response(perg)) + "\n")
    txt.insert(END,str(resposta.confidence*100) + " %\n")
    txt_send.delete('1.0',END)
    txt.configure(state=DISABLED)

janela.mainloop()
