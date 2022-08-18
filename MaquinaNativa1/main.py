from tkinter import *
import time
from tkinter import filedialog #Librería para seleccionar archivo
from tkinter import ttk as ttk #Tkinter
from usuarios import Usuario
from tkinter import messagebox as messagebox

root = Tk() #Crea un objeto Tkinter
usuarios = []
passUser = StringVar()
nameUsuario = StringVar()
mainFrame = Frame(root) #Crea un frame contenedor
fileLabel = Label(mainFrame,text = "") #Crea una etiqueta para mostar el archivo subido
fileLabel.grid(column=0,row=2) #Lo coloca en la columna 0 y fila 2 de 'mainFrame'

def createGUI():
    # ventana principal
    #root = Tk()
    root.title("Login Cifrado USRP")

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
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0,row=3)

    #entradas de textos

    passUser.set("")
    passEntry = Entry(mainFrame,textvariable=passUser, show="*")
    passEntry.grid(column=1,row=3)

    #BOTONES
    
    #Botón Cargar Archivo
    loadFileButton = ttk.Button(
    mainFrame, text = "Cargar Archivo", command=openFile)
    loadFileButton.grid(column=1,row=2,ipadx=5,ipady=5,pady= 10,padx= 10)
    
    #Botón Enviar
    sendButton = ttk.Button(
    mainFrame, text = "Enviar", command=send)
    sendButton.grid(column=1,row=5,ipadx=5,ipady=5,pady= 10,padx= 10)
    
    root.mainloop() #Mantiene la ventana abierta

def send():
    with open("authen.txt","w",encoding= "utf-8") as f:
        f.write(passUser.get()) #Contraseña
        # f.write("\n")           #Retorno de carro
        # f.write(fileLabel.cget("text")) #Nombre del Archivo
    root.destroy()
     
def openFile():
    file = filedialog.askopenfilename(title="Abrir") #Abre la ventana para examinar archivo
    with open(file,"rb") as f1:
        data = f1.read() # Lo lee
    with open("data.bin","wb") as f2:
        f2.write(data)  #Lo guarda con un nombre único
    fileLabel.config(text=file[-30:]) #Escribe el nombre del archivo recortado
    


start = time.process_time()

if __name__ == '__main__':
    createGUI()

end = time.process_time()

print(end - start)