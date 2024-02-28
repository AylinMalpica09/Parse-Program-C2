from tkinter import filedialog
import customtkinter
import tkinter as tk
from analizadorSintactico import analizador_sintactico


customtkinter.set_appearance_mode("light") #"system"|"light"|"dark"
app = customtkinter.CTk()
app.title("Tabla Predictiva Grammar 4")
app.geometry("700x600")
app.grid_columnconfigure((0), weight=1)
app.resizable(False, False)

titleDato1 = customtkinter.CTkLabel(app, text="Ingresa tu cadena:", text_color="#4A4A4A", font=("Open Sans Regular",14), width=500, height=20)
titleDato1.grid(row=3, column=0, padx=0, pady=(0,13))

txtcadena = customtkinter.CTkEntry(app, placeholder_text="", width=450, height=50, corner_radius=2, border_color="#FD94FF", font=("Open Sans Regular", 14))
txtcadena.grid(row=4, column=0, padx=0, pady=(0,20))

tolerancia = customtkinter.CTkEntry(app, placeholder_text="", width=450, height=150, corner_radius=2, border_color="#FD94FF", font=("Open Sans Regular", 12))
tolerancia.grid(row=6, column=0, padx=0, pady=(0,20))

def getData():
    entrada = txtcadena.get()
    resultado = analizador_sintactico(entrada)
    print("La cadena a evaluar es:", entrada) 
    print("La cadena evaluada es:", resultado) 
    tolerancia.delete(0, 'end')  # Borra el contenido actual
    lineas = resultado.split(']\n')  # Dividir el resultado cada vez que detectes un "]"
    for linea in lineas:
        # Agregar el "]" nuevamente para que no se pierda en la división
        linea += ']'
        tolerancia.insert('end', linea + '\n')
    #tolerancia.insert('end', "Resultado: " + resultado)  # Inserta el nuevo texto


buttonEmpezar = customtkinter.CTkButton(app, text="Empezar", width=250, height=20, font=("Open Sans Bold",14), text_color="#FFFFFF", fg_color="#FD94FF", hover_color=("#F328F8","#F328F8"), hover=True, corner_radius=2, command=getData)
buttonEmpezar.grid(row=9, column=0, padx=0, pady=(0,0))

app.mainloop()


#PRUEBA VALIDA
#automata alfabeto : 1,a,2,b; aceptacion : 1; fin 