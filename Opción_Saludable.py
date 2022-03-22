from tkinter import *
from subprocess import call
from modulos import *

print("\n")
print(("  Hola gracias por entrar a nuestra app  ").center(80, "="))
print("Porfavor a continuacion responde las siguientes preguntas para saber que no eres un bot")
print("-"*80)
a = int(input("Por favor ingresa un primer numero entero positivo: "))
b = int(input("Por favor ingresa un segundo numero entero positivo: "))
print("-"*80)
#contador de respuestas
respuestas = 0
#preguntas
resultado1 = int(input("\n¿Cual es la suma de los dos numeros que ingresaste?\n"))
if resultado1 == suma(a,b):
    respuestas += 1
    print("Respuesta correcta")
else:
    print("Lo siento, no queremos robots aca")
    exit()
resultado2 = int(input("\n¿Cual es la multiplicacion de ambos numeros?\n"))
if resultado2 == multi(a,b):
    respuestas += 1
    print("Respuesta correcta")
else:
    print("Lo siento, no queremos robots aca")
    exit()
resultado3 = int(input("\n¿Cual es la suma de los digitos del año actual?\n"))
if resultado3 == año():
    respuestas += 1
    print("Respuesta correcta")
else:
    print("Lo siento, no queremos robots aca")
    exit()
#final
if respuestas == 3:
    print("\n-->FELICIDADES,Pasaste con exito la prueba\n")
    print("-"*70)
    print (("Bienvenido a Tu Opcion Saludable").center(70, "="))
    print("-"*70)
    print("Se acaba de abrir una ventana, ve a mirarla para el registro respectivo ")
    print("-"*70)
    root = Tk()
    root.title("Opción Saludable - Inicio")
    root.geometry("500x650")
    root.resizable(False,False)
    #funcion registro
    def abrir_registro():
        root.destroy()
        call(["python", "registro.py"])

    #Barra del menu
    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Guardar")
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Pegar")

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    #titulo dentro del programa
    titulo = Label(root, text="OPCION SALUDABLE", bg="#FEF5E7", font=("Sans Serif",25), width="500")
    titulo.pack()
    #imagen
    imagen = PhotoImage(file="img/corazon.gif")
    Label(root, image=imagen, bd=0, relief="solid").pack()
    #alumnos
    label = Label(root, text="Proyecto hecho por: Ramos Tito, Alex & Barrios Puchoc, Luis",bg="#FAE5D3",font=("Sans Serif",10), width="500")
    label.pack(anchor=CENTER)
            
    #Boton de ingreso
    Button(root, text="INGRESAR", disabledforeground="deep pink",bg="#943126", width=40, height=3, relief="ridge", 
    borderwidth=5, font=("Sans Serif",25),fg="white",command = abrir_registro).pack()

    root.mainloop()