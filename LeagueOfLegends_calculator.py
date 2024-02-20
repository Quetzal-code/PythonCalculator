"""League of Legends Calculator"""""
import tkinter as tk
import re

DARK_BLUE = '#005A82'
GOLD = '#C89B3C'
GRAY = '#A09B8C'
BLACK = '#010A13'

def mostrar(value):
    display.insert(tk.END, value)

calculadora = tk.Tk()
calculadora.title("Calculadora")
calculadora.iconbitmap("Calculator.ico")
calculadora.geometry("260x380+170+120")
calculadora.resizable(width=False, height=False)

def son_numeros(expression):
    texto = re.compile(r'^[-+*/0-9).(\s]+$')
    return bool(texto.fullmatch(expression))

def borrar_todo():
    display.delete(0, tk.END)

def borra():
    current_text = display.get()
    display.delete(len(current_text)-1, tk.END)

def calcular_resul():
    operacion= display.get()
    if  son_numeros(operacion):
        try:
            result = eval(operacion)
            borrar_todo()
            display.insert(0, result)
        except (SyntaxError, NameError, ZeroDivisionError) as e:
            borrar_todo()
            if isinstance(e, ZeroDivisionError):
                display.insert(0, "Error: División por cero")
            else:
                display.insert(0, "Error: Expresión inválida")
    else :
        borrar_todo()
        display.insert(0, "No valido")

display = tk.Entry(calculadora, font=('Arial', 24), bg=GRAY, fg=BLACK, borderwidth=2, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

button_frame = tk.Frame(calculadora, bg=DARK_BLUE)
button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

calculadora.grid_rowconfigure(0, weight=1)
calculadora.grid_columnconfigure(0, weight=1)
button_frame.grid_rowconfigure(0, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('Del', 4, 1),('C', 4, 2), ('+', 4, 3), 
    ('.', 5, 2), ('=', 5, 3),
]

def crear_boton(text, row, column):
    button_commands = {'C': borrar_todo, '=': calcular_resul, 'Del': borra, '=': calcular_resul}
    command = button_commands.get(text, lambda: mostrar(text))

    button = tk.Button(button_frame, text=text, command=command, 
                       font=('Arial', 18), bg=GOLD, fg=BLACK)
    button.grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
    return button


for text, row, column in buttons:
    if text == '0':
        crear_boton(text, row, column).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
    else:
        crear_boton(text, row, column).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)

calculadora.mainloop()