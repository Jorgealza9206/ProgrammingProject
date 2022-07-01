from tkinter import *
from tkinter import ttk as ttk
from usuarios import Usuario
from tkinter import messagebox as messagebox

root = Tk()
usuarios = []
passUser = StringVar()
nameUsuario = StringVar()

def createGUI():
    # ventana principal
    #root = Tk()
    root.title("Login Usuario")

    # mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width = 480, height = 320)#, bg="lightblue")

    #textos y titulos
    titulo = Label(mainFrame, text="Login de usuario con Python", font=("Arial",24))
    titulo.grid(column=0, row=0, padx = 10, pady = 10, columnspan=2)

    nameLabel = Label(mainFrame, text = "Nombre: ")
    nameLabel.grid(column=0,row=1)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0,row=2)

    #entradas de textos

    nameUsuario.set("")
    nameEntry = Entry(mainFrame,textvariable=nameUsuario)
    nameEntry.grid(column=1,row=1)


    passUser.set("")
    passEntry = Entry(mainFrame,textvariable=passUser, show="*")
    passEntry.grid(column=1,row=2)

    #BOTONES
    newBut = ttk.Button
    initSesionButton = ttk.Button(mainFrame, text = "Iniciar sesión", command=initSession)
    initSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,pady= 10,padx= 10)

    registerButton = ttk.Button(mainFrame, text = "Registrarse", command=registerUser)
    registerButton.grid(column=0,row=3,ipadx=5,ipady=5,pady= 10,padx= 10)
    
    root.mainloop()

def initSession():
    for user in usuarios:
        if user.name == nameUsuario.get():
            test = user.connect(passUser.get())
            if test:
                messagebox.showinfo("Conectado",f"Se inició sesión en [{user.name}] con éxito")
            else:
                messagebox.showerror("Error","contraseña incorrecta")
            break
    else:
        messagebox.showerror("Error","Usuario no existe")

def registerUser():
    name = nameUsuario.get()
    passwd = passUser.get()
    newUser = Usuario(name,passwd)
    usuarios.append(newUser)
    messagebox.showinfo("Registro Exitoso",f"Se registró el usuario [{name}] con éxito!!")
    nameUsuario.set("")
    passUser.set("")
    
if __name__ == '__main__':
    #user1 = Usuario(input("Ingrese un nombre: "),input("Ingrese una contraseña: "))
    user1 = Usuario("Lucas","1234")
    usuarios.append(user1)
    createGUI()