import customtkinter
from parserLogic import parse

customtkinter.set_appearance_mode("light") #"system"|"light"|"dark"
app = customtkinter.CTk()
app.title("Tabla Predictiva Grammar 4")
app.geometry("700x720")
app.grid_columnconfigure((0), weight=1)
app.resizable(False, False)

titleDato1 = customtkinter.CTkLabel(app, text="Ingresa tu cadena:", text_color="#4A4A4A", font=("Open Sans Regular",14), width=500, height=20)
titleDato1.grid(row=3, column=0, padx=0, pady=(0,13))

txtcadena = customtkinter.CTkEntry(app, placeholder_text="", width=450, height=50, corner_radius=2, border_color="#FD94FF", font=("Open Sans Regular", 14))
txtcadena.grid(row=4, column=0, padx=0, pady=(0,20))

frame_resultado = customtkinter.CTkFrame(app, width=450)
frame_resultado.grid(row=6, column=0, padx=0, pady=(0,20))

def getData():
    entrada = txtcadena.get()
    resultado = parse(entrada)
    #print("La cadena a evaluar es:", entrada) 
    print("La cadena evaluada es:\n", resultado) 
    
    for widget in frame_resultado.winfo_children():
        widget.destroy()
    

    for i, linea in enumerate(resultado.split('\n')):
        customtkinter.CTkLabel(frame_resultado, text=linea).grid(row=i, column=0, sticky="w")

buttonEmpezar = customtkinter.CTkButton(app, text="Empezar", width=250, height=20, font=("Open Sans Bold",14), text_color="#FFFFFF", fg_color="#FD94FF", hover_color=("#F328F8","#F328F8"), hover=True, corner_radius=2, command=getData)
buttonEmpezar.grid(row=9, column=0, padx=0, pady=(0,0))

app.mainloop()

#PRUEBA VALIDA
#automata alfabeto : 1,a,2,b; aceptacion : 1; fin 