# PythonCalculator
A calculator with Python based in the popular game League Of Legends

# Calculadora Simple

Esta es una calculadora simple con interfaz gráfica desarrollada en python utilizando la biblioteca tkinter.

## Funcionalidades

1. **Operaciones Básicas:**
   - Suma
   - Resta
   - Multiplicación
   - División

2. **Operaciones Adicionales:**
   - Punto decimal para números decimales.
   - Botón "C" para borrar la pantalla.

3. **Uso Sencillo:**
   - Ingresa los números y realiza operaciones haciendo clic en los botones correspondientes.
   - El botón "=" muestra el resultado.

## Personalización

Puedes personalizar la apariencia de la calculadora ajustando los colores en el código fuente Python. Actualmente, la calculadora utiliza colores de fondo y texto específicos.

```python
# Configuración de colores
root.configure(bg="#005A82")  # Color de fondo de la ventana
entry = tk.Entry(root, font=("Arial", 20), justify="right", bg="#005A82", fg="#C89B3C")  # Color de fondo y texto del área de entrada
btn = tk.Button(root, text="7", font=("Arial", 15), padx=20, pady=10, bg="#C89B3C", fg="#005A82")  # Color de fondo y texto de los botones
```

Ejecución
Asegúrate de tener Python instalado. Puedes ejecutar la calculadora ejecutando el siguiente comando en tu terminal:

```python
python LeagueOfLegends_calculator.py
```

Contribuciones
¡Contribuciones son bienvenidas! Si encuentras algún error o tienes mejoras sugeridas, no dudes en abrir un problema o enviar un pull request en el repositorio.

Quetzal Uzcategui