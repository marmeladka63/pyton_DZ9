
from tkinter import *
import random, time

def victory(comb): #Условие выигрыша
    global move
    if (move[0] == comb and move[1] == comb and move[2] == comb) or (move[3] == comb and move[4] == comb and move[5] == comb)\
        or (move[6] == comb and move[7] == comb and move[8] == comb) or (move[0] == comb and move[3] == comb and move[6] == comb) \
        or (move[1] == comb and move[4] == comb and move[7] == comb) or (move[2] == comb and move[5] == comb and move[8] == comb)\
        or (move[0] == comb and move[4] == comb and move[8] == comb) or (move[2] == comb and move[4] == comb and move[6] == comb) :
        return True

def click(pl):  # функиця обратботки нажатия кнопок в игре
    
    global move_list
    global count

    move[pl] = 'X' 
    button[pl].config(text='X', bg="white", state='disabled') 
    move_list.remove(pl) #удаляем данные о нажатой кнопке из списка

    if pl == 4:   # обрабатывается стратегия игрока, при нажатии на центральную клетку
        
        bot = random.choice(move_list) # Игра компьютера
        move[bot] = 'O'
        
    elif pl!=4 and count == 0:
        bot = 4

    if count > 0:
        bot = 8 - pl # логика компьютера при двух закрытых в ряд или  в диагональ клетках игроком
        if bot not in move_list: #Проверка на нажатую кнопку
            try:   # Обработка исключения 
                bot = random.choice(move_list)
            except IndexError:
                label['text'] = 'Игра окончена!'

    time.sleep(0.2) #задержка по времении при нажатии 
    button[bot].config(text='O', bg="white", state='disabled')
    if victory('X'):
        label['text'] = 'Ура Вы выиграли!'
    elif victory('O'):
        label['text'] = 'ПЕчалька Вы проиграли!'
    else:
        if (len(move_list) >1): # если в списке еще есть номера кнопок
            move_list.remove(bot) # удаляем из него номер кнопки, нажатый компьютером
        else:
            label['text'] = 'Игра окончена!'# Если нажали все кнопки - игра окончена 

    count +=1

move =[None]*9 # Данные о ходах
move_list = list(range(9)) #Лист с числами от 0 до 8 для понимания какие ячейик остались в игре
count = 0 # Счетчик ходов

root = Tk() #Создание корневого окна
label =Label(width=20, text ="КРЕСТИКИ - НОЛИКИ", font=('Arial',20) )
label.grid(column=0, row=0) 
button =[Button(width=5,height=2,font=('Arial',30), bg="blue", command=lambda x = i: click(x) ) for i in range(9)] #создание кнопок

label.grid(column=0, row=0, columnspan=3) 
r = 1
c =0
for i in range(9): #Расставляем кнопки в окне игры
    button[i].grid(row=r, column=c)
    c +=1
    if c ==3:
        r +=1
        c = 0

root.mainloop()

# window = Tk()  
# window.title("Добро пожаловать в приложение PythonRu")  
# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)  
# window.mainloop()