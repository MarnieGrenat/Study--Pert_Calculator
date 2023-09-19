# Imports externos
import os
import base64
from tkinter import *
from tkinter import ttk

# Imports internos
from icon import icon
from calculator import Estimate  


data = Estimate(0, 0, 0)  


def validate_input():
    optimistic_value = optimistic.get()
    nominal_value = nominal.get()
    pessimistic_value = pessimistic.get()

    if optimistic_value.isdigit() and nominal_value.isdigit() and pessimistic_value.isdigit():
        optimistic_value = float(optimistic_value)
        nominal_value = float(nominal_value)
        pessimistic_value = float(pessimistic_value)

        # Cálculo do valor de PERT
        data = Estimate(optimistic_value, nominal_value, pessimistic_value)
        estimates = data.get_estimates()

        # Valores exibidos na tela
        result_label.config(text=f"[Deadline: {estimates['deadline']}]")
        result_label2.config(text=f"[Atraso máximo estimado: {estimates['lateness']}]")
    else:
        result_label.config(text="[Erro: Valores inválidos! Entre valores inteiros positivos.]")

def showPertMethod():
    """ Janela pop-up """
    pert_window = Toplevel(root)
    
    pert_info = """
    O método PERT (Program Evaluation and Review Technique) é uma técnica usada para estimar o tempo necessário para concluir um projeto.\n
    Ele leva em consideração três estimativas de duração:\n
    
    - Estimativa Otimista: O menor tempo que uma tarefa pode ser concluída.\n
    - Estimativa Nominal: A melhor estimativa do tempo necessário.\n
    - Estimativa Pessimista: O maior tempo que uma tarefa pode ser concluída.\n
    
    Com base nessas estimativas, o PERT calcula a estimativa mais provável e o atraso máximo esperado para o projeto.\n
    Nesta calculadora, todas as estimativas são calculadas em dias.\n
    \nDesenvolvedor da aplicação: Gabriela Dellamora Paim
    GitHub: github.com/marniegrenat
    
    """
    
    pert_window.title("Sobre o Método PERT")



    # Evita bug do "quadrado cinza" dentro da janela 
    pert_window.grid_rowconfigure(0, weight=1)
    pert_window.grid_columnconfigure(0, weight=1)
    
    pert_label = Label(pert_window, text=pert_info, padx=20, pady=20)
    pert_label.grid(row=0, column=0, sticky="nsew")

    # Centralize a janela pop-up no centro da janela principal
    # Define tamanho min e max da janela
    pert_window.minsize(600, 200)
    pert_window.maxsize(600, 200)
    pert_window.geometry(f"900x300+{root.winfo_x() + 320}+{root.winfo_y() + 220}")


## MAIN
root = Tk()
root.title("Calculador de Entregas")


root.geometry("320x320") 
root.minsize(300, 320)
root.maxsize(300, 320)

# src: 
icondata= base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()
root.wm_iconbitmap(tempFile)
## Delete the tempfile
os.remove(tempFile)

# Adicione margem para a janela
root.geometry("+10+10")



# Evita bug do "quadrado cinza" dentro da janela 
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = ttk.Frame(root, padding="30 30 30 30")  # Adicione margem para o frame
frame.grid(column=0, row=0, sticky=(N, W, E, S))
#### Blocos de input
optimistic = ttk.Entry(frame, width=7)
optimistic.grid(column=0, row=0, pady=(0, 5))

nominal = ttk.Entry(frame, width=7)
nominal.grid(column=0, row=1, pady=(0, 5))

pessimistic = ttk.Entry(frame, width=7)
pessimistic.grid(column=0, row=2, pady=(0, 5))
####

# Labels dos inputs
ttk.Label(frame, text="Estimativa Otimista, em dias.").grid(column=1, row=0)
ttk.Label(frame, text="Estimativa Nominal, em dias.").grid(column=1, row=1)
ttk.Label(frame, text="Estimativa Pessimista, em dias.").grid(column=1, row=2)

# Label para exibir o resultado bruto
result_label = ttk.Label(frame, text="")
result_label.grid(column=1, row=5, pady=(0, 5))

# Label para exibir o resultado + desvio-padrao
result_label2 = ttk.Label(frame, text="")
result_label2.grid(column=1, row=6, pady=(0, 5))  

ttk.Button(frame, text="Calcular", command=validate_input).grid(column=1, row=4, pady=(0, 5))
ttk.Button(frame, text="Sobre o método PERT", command=showPertMethod).grid(column=1, row=7, pady=(0, 5))  # Ajuste a posição conforme necessário

## RODAPÉ
footer_frame = ttk.Frame(root)
footer_frame.grid(column=0, row=1, sticky=(W, E, S))

version_label = ttk.Label(footer_frame, text="Version: 1.0.1")
version_label.grid(column=0, row=0, padx=10, pady=(5, 0))

developer_label = ttk.Label(footer_frame, text="Developer: Gabriela Dellamora Paim ")
developer_label.grid(column=1, row=0, padx=10, pady=(5, 0))

## LOOP
if __name__ == '__main__':
    root.mainloop()
