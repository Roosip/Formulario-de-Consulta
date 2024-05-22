# importando a biblioteca tkinter para fazer a interface grafica
from tkinter import *

############### Cores ###############
cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#038cfc"   # azul
cor7 = "#ef5350"   # vermelha
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # sky blue

############### Criando janela ###############

janela = Tk() # Criando a janela
janela.title("Painel de Consulta") #adicionando o titulo da janela
janela.geometry('1024x720') # definindo a dimensão da janela
janela.configure(background=cor9) # definindo a cor de fundo da janela
# janela.resizable(width=FALSE, height=FALSE) # faz com que o usuário não consisa redimensionar a janela

janela.mainloop()