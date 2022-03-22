from tkinter import *
from tkinter import messagebox
from subprocess import call

# mi root se llamara registro, el root es la raiz del contenedor
registro = Tk()
registro.title("Registro")
registro.geometry("400x300")
registro.resizable(False,False)
#titulo dentro
titulo = Label(text = "Registro de Nuevos Usuarios", bg = "#FEF5E7", fg = "black", width = "500", height = "2", font=("Sans Serif",15))
titulo.pack()

#funcion del boton registrar
def registrado():
    respuesta = messagebox.askyesno("Registro","¿ Desea seguir a la siguiente ventana de nuestros productos ?")
    if respuesta == 1:
        # añado los datos ingresados a un nuevo archivo
        email_info = email.get()
        password_info= password.get()
        usuario = open("datos_usuario.txt","w")
        usuario.write("Correo: "+email_info+"\n")
        usuario.write("Contraseña: "+password_info+"\n")
        usuario.close()
        registro.destroy()
        call(["python", "productos1.py"])
    else:
        return breakpoint
    print("\nNuevo Usuario Registrado: \nCorreo: {} | Contraseña: {}".format(email_info, password_info))

# labels
email_label = Label(text = "Email Address:")
email_label.place(x = 22, y = 70)
password_label = Label(text = "Password:")
password_label.place(x = 22, y = 130)

#entradas
email = StringVar()
password = StringVar()
 
email_entry = Entry(textvariable = email, width = "60")
password_entry = Entry(textvariable = password, width = "60",  show = "*")
 
email_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)

# Boton registrar
registrar = Button(registro,text = "REGISTRAR", width = "30", height = "2", bg = "#943126", padx="50", fg="#FDFEFE", command=registrado)
registrar.place(x = 42, y = 220)

# en una interface siempre esta en constante loop
registro.mainloop()