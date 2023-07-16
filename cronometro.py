from tkinter import Tk, Label, Button, Frame

# Definição das cores
COR_PRETO = '#000000'
COR_BRANCO = '#FFFFFF'
COR_VERDE = '#21C25C'
COR_VERMELHO = '#EB463B'
COR_CINZA = '#DEDCDC'
COR_AZUL = '#3080F0'

# Criação da janela principal
janela = Tk()
janela.title('')
janela.geometry('380x180')
janela.configure(bg=COR_PRETO)
janela.resizable(width=False, height=False)

# Variáveis globais
global tempo
global contador
global rodar
global limitador

limitador = 59
tempo = "00:00:00"
contador = -5
rodar = False

# Função para iniciar o cronômetro
def iniciar():
    global contador
    global tempo
    global limitador

    if rodar:
        if contador <= -1:
            inicio = f'Começando em {abs(contador)}'
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        else:
            label_tempo['font'] = 'Times 50 bold'
            temporaria = str(tempo)
            hora, minuto, segundo = map(int, temporaria.split(":"))

            hora = int(hora)
            minuto = int(minuto)

            if segundo >= limitador:
                contador = 0
                minuto += 1
            else:
                segundo += 1

            segundo = str(0) + str(segundo)
            minuto = str(0) + str(minuto)
            hora = str(0) + str(hora)

            temporaria = str(hora[-2:] + ":" + str(minuto[-2:]) + ":" + str(segundo[-2:]))

            label_tempo['text'] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1

# Função para iniciar o cronômetro quando o botão "Iniciar" é pressionado
def start():
    global rodar
    rodar = True
    iniciar()

# Função para pausar o cronômetro quando o botão "Pausar" é pressionado
def pausar():
    global rodar
    rodar = False

# Função para reiniciar o cronômetro quando o botão "Reiniciar" é pressionado
def reiniciar():
    global tempo
    global contador

    contador = 0
    tempo = "00:00:00"
    label_tempo['text'] = tempo

# Criação dos componentes da interface
label_cronometro = Label(janela, text='cronômetro', font=('Arial 10'), bg=COR_PRETO, fg=COR_BRANCO)
frame_contador = Frame(janela, bg=COR_PRETO)
label_tempo = Label(frame_contador, text=tempo, font=('Time 50 bold'), bg=COR_PRETO, fg=COR_VERMELHO)

label_cronometro.place(x=10, y=10)  # Posiciona o label "cronômetro" na janela
frame_contador.place(relx=0.5, rely=0.5, anchor='center')  # Posiciona o frame do contador no centro da janela
label_tempo.pack()  # Empacota o label do contador dentro do frame

label_iniciar = Button(janela, width=8, height=1, text='Iniciar', bg=COR_PRETO, fg=COR_BRANCO, command=start)
label_pausar = Button(janela, width=8, height=1, text='Pausar', bg=COR_PRETO, fg=COR_BRANCO, command=pausar)
label_reiniciar = Button(janela, width=8, height=1, text='Reiniciar', bg=COR_PRETO, fg=COR_BRANCO, command=reiniciar)

label_iniciar.place(x=35, y=120)  # Posiciona o botão "Iniciar" na janela
label_pausar.place(x=145, y=120)  # Posiciona o botão "Pausar" na janela
label_reiniciar.place(x=255, y=120)  # Posiciona o botão "Reiniciar" na janela

janela.mainloop()