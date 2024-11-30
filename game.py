from tkinter import *
import random
from string import ascii_uppercase as alp


list_height = [i for i in alp]
len_alp = len(alp)


bottom_line = int(input(f"Введите нижнюю границу интервала (>= 4): "))
top_line = int(input(f"Введите верхнюю границу интервала (>= {bottom_line}): "))


def clicked():
    key = ''
    for _ in range(3):
        part_weight = 0
        part_key = ''
        while len(part_key) < 4 and len(part_key) < bottom_line:
            height_letter = random.randint(1, len_alp + 1)
            if part_weight + height_letter <= top_line:
                part_weight += height_letter
                part_key += alp[height_letter - 1]
        key += f'-{part_key}'
    lbl2.configure(text=key[1:])



window = Tk()
window.title('Sims 4')
window.geometry('700x600')


bg = PhotoImage(file = "background_sims.png") 
label1 = Label(window, image = bg) 
label1.place(x = 0, y = 0) 


lbl1 = Label(window, text = 'SIMS 4', font = ('Century', 50), bg="#008000", fg="white")
lbl1.place(relx = 0.5, rely = 0.1, anchor = CENTER)


lbl2 = Label(window, text = 'XXXX-XXXX-XXXX', font = ('Century', 30), bg="#008000")
lbl2.place(relx = 0.5, rely = 0.5, anchor = CENTER)


btn = Button(window, text = 'Generate', font = ('Century', 15), command = clicked)
btn.place(relx = 0.5, rely = 0.59, anchor = CENTER)


window.mainloop()

