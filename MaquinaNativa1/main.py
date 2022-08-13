from tkinter import *
from tkinter import filedialog
from tkinter import ttk as ttk
from usuarios import Usuario
from tkinter import messagebox as messagebox

root = Tk()
usuarios = []
passUser = StringVar()
nameUsuario = StringVar()
mainFrame = Frame(root)
fileLabel = Label(mainFrame,text = "")
fileLabel.grid(column=0,row=2) 

def createGUI():
    # ventana principal
    #root = Tk()
    root.title("Login Usuario")

    # mainFrame
    mainFrame.pack(side=BOTTOM)
    mainFrame.config(width = 480, height = 320)#, bg="lightblue")
    
    #imagen de la UD
    img = PhotoImage(file="logo_ud.png")
    imgLabel = Label(mainFrame, image=img)
    imgLabel.grid(column=0, row=1, padx = 10, pady = 10, columnspan=2)

    #textos y titulos
    titulo = Label(mainFrame, text="Autenticación USRP", font=("Arial",24))
    titulo.grid(column=0, row=0, padx = 10, pady = 10, columnspan=2)

    # fileLabel = Label(mainFrame,text = "")
    # fileLabel.grid(column=0,row=2) 
    nameLabel = Label(mainFrame, text = "Nombre: ")
    nameLabel.grid(column=0,row=3)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0,row=4)

    #entradas de textos

    nameUsuario.set("")
    nameEntry = Entry(mainFrame,textvariable=nameUsuario)
    nameEntry.grid(column=1,row=3)

    passUser.set("")
    passEntry = Entry(mainFrame,textvariable=passUser, show="*")
    passEntry.grid(column=1,row=4)

    #BOTONES
    
    loadFileButton = ttk.Button(
    mainFrame, text = "Cargar Archivo", command=openFile)
    loadFileButton.grid(column=1,row=2,ipadx=5,ipady=5,pady= 10,padx= 10)
    
    sendButton = ttk.Button(
    mainFrame, text = "Enviar", command=send)
    sendButton.grid(column=1,row=5,ipadx=5,ipady=5,pady= 10,padx= 10)
    
    root.mainloop()

def send():
    with open("authen.txt","w",encoding= "utf-8") as f:
        f.write(nameUsuario.get())
        f.write("\n")
        f.write(passUser.get())
        f.write("\n")
        f.write(fileLabel.cget("text"))
    root.destroy()
     
def openFile():
    file = filedialog.askopenfilename(title="Abrir")
    with open(file,"rb") as f1:
        data = f1.read()
    with open("data.bin","wb") as f2:
        f2.write(data)
    fileLabel.config(text=file[-30:])
    
if __name__ == '__main__':
    createGUI()