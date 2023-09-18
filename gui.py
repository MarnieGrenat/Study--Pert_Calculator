from calculator import *
from tkinter import *
from tkinter import ttk

def set_estimate_values(data, optimistic, nominal, pessimistic):
    pass

def showPertMethod():
    pass

data = Estimate(0, 0, 0)

## MAIN
root = Tk()
root.title("Calculador de Entregas")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))  # Adicione esta linha para fazer o frame aparecer
root.geometry("300x200")  # Define a largura como 800 pixels e a altura como 600 pixels


optimistic = ttk.Entry(frame, width=7)
optimistic.grid(column=0, row=0)
nominal = ttk.Entry(frame, width=7)
nominal.grid(column=0, row=1)
pessimistic = ttk.Entry(frame, width=7)
pessimistic.grid(column=0, row=2)

ttk.Label(frame, text="Estimativa Otimista, em dias.").grid(column=1, row=0)
ttk.Label(frame, text="Estimativa Nominal, em dias.").grid(column=1, row=1)
ttk.Label(frame, text="Estimativa Pessimista, em dias.").grid(column=1, row=2)

ttk.Button(frame, text="Gerar Estimativa de Entrega", command=lambda: set_estimate_values(data, optimistic, nominal, pessimistic)).grid(column=1, row=3)
ttk.Button(frame, text="Sobre o método PERT", command=showPertMethod).grid(column=1, row=4)

## PERT METHOD

## LOOP
root.mainloop()
