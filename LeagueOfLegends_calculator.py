"""League of Legends Calculator"""""
import tkinter as tk
import re

# Define los colores
DARK_BLUE = '#005A82'
GOLD = '#C89B3C'
GRAY = '#A09B8C'
BLACK = '#010A13'

# Función para agregar el valor al display
def mostrar(value):
    display.insert(tk.END, value)

# Crea la ventana principal
root = tk.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.resizable(width=False, height=False)
def son_numeros(expression):
    """verificar que es una operacion matemática"""
    texto = re.compile(r'^[-+*/0-9).(\s]+$')
    return bool(texto.match(expression))

# Función para borrar el display
def clear_display():
    display.delete(0, tk.END)

# Función para calcular la expresión
def calculate_expression():
    operacion= display.get()
    if  son_numeros(operacion):
        try:
            result = eval(operacion)
            clear_display()
            display.insert(0, result)
        except Exception as e:
            clear_display()
            display.insert(0, "Error")
    else :
        clear_display()
        display.insert(0, "No valido")

# Crea el display
display = tk.Entry(root, font=('Arial', 24), bg=GRAY, fg=BLACK, borderwidth=2, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Crea un frame para los botones
button_frame = tk.Frame(root, bg=DARK_BLUE)
button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

# Configura los pesos de las filas y columnas
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
button_frame.grid_rowconfigure(0, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Define los botones y sus posiciones en una lista de tuplas
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 2), ('+', 4, 3), ('.', 5, 2),
]

# Función para crear botones
def create_button(text, row, column):
    if text == 'C':
        command = clear_display
    elif text == '=':
        command = calculate_expression
    else:
        command = lambda value=text: mostrar(value)

    button = tk.Button(button_frame, text=text, command=command, 
                       font=('Arial', 18), bg=GOLD, fg=BLACK)
    button.grid(row=row, column=column)
    return button

# Crea y coloca los botones en la grid
for text, row, column in buttons:
    if text == '0':
        # El botón '0' se expande en dos columnas
        create_button(text, row, column).grid(row=row, column=column, columnspan=2, sticky='nsew', padx=5, pady=5)
    else:
        create_button(text, row, column).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)

# Botón de igual
equal_button = create_button('=', 5, 3)
equal_button.grid(columnspan=2, sticky='nsew')
equal_button.config(command=calculate_expression)

# Ejecuta la aplicación
root.mainloop()