from tkinter import *
from subprocess import call
from tkinter import messagebox as MessageBox
def agregar():
    naranja = num.get()
    comprado2 = naranja*2.9
    compra2 = open("compras.txt","a")
    compra2.write("Naranja: {}\n".format(comprado2))
    cantidad_entry.delete(0, END)

#compra completada
def completa():
    MessageBox.showinfo("Gracias - Omedeto", "Se ha generado tu boleta, ve a revisarla")
    root.destroy()
    call(["python", "total.py"])

#boton siguiente
def forward():
    root.destroy()
    call(["python", "productos3.py"])

#boton atras
def back():
    root.destroy()
    call(["python", "productos1.py"])

# Configuración de la raíz
root = Tk()
root.title("Opción Salusable - Productos")
root.config(bd=25)
root.geometry("650x350")
root.resizable(False,False)
#titulo
titulo = Label(root, text="NUESTROS PRODUCTOS", bg="#FEF5E7", font=("Sans Serif",25), width="500")
titulo.pack()

#imagen
imagen = PhotoImage(file="img/naranja.gif")
Label(root, image=imagen, width=250, height=200, relief="ridge", borderwidth=5,fg="white").pack(side="left")

#titulo de compra
desea = Label(root,text="¿Deseas comprar este producto?",font=("Sans Serif",15))
desea.place(x = 300, y= 100)
#producto
producto = Label(root,text="NARANJAS : S/.2.90 c/u ",font=("Sans Serif",20), fg="orange")
producto.place(x = 300, y= 130)

#cantidad
titulo02 = Label(root,text="Cantidad que desea comprar: ",font=("Sans Serif",10)).place(x=320, y= 180)
num = IntVar()
cantidad_entry = Entry(root,textvariable = num, width = "5")
cantidad_entry.place(x = 500, y=180)

#agregar
button_accept=Button(root, text="SI, AGREGAR", padx=7, command= agregar).place(x=390, y=215)

#botones
button_sig=Button(root, text="PREV", padx=7,command=back).place(x=300, y=250)
button_completo=Button(root, text="COMPRA COMPLETA", padx=7,command=completa).place(x=370, y=250)
button_prev=Button(root, text="SIG", padx=7,command=forward).place(x=520, y=250)

# Finalmente bucle de la aplicación
root.mainloop()