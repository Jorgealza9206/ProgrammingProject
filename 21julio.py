import subprocess
import tkinter as tk 
import os
import tkinter


def createNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("500x400")
    newWindow.config(bg="white")

    etiqueta0 = tkinter.Label(newWindow, text = "Universidad Distrital ", font = "tomas 15",bg="orange")
    etiqueta0.pack(fill = tkinter.X)

    etiqueta1 = tkinter.Label(newWindow, text = "Francisco José de Caldas", font = "tomas 15",bg="orange")
    etiqueta1.pack(fill = tkinter.X)

    etiqueta = tkinter.Label(newWindow, text = "Sistema de transmisión ",bg="white", font = "Verdana 17", pady =5)
    etiqueta4 = tkinter.Label(newWindow, text = " para AM ",bg="white", font = "Verdana 17", pady =5)

    etiqueta.pack(fill = tkinter.X)
    etiqueta4.pack(fill = tkinter.X)


    etiqueta6 = tkinter.Label(newWindow, text = "Mensaje 2 s: Estado de Emergencia", font = "tomas 9",bg="yellow")
    etiqueta6.pack(fill = tkinter.X)
    etiqueta7 = tkinter.Label(newWindow, text = "Mensaje 4 s: Este es un mensaje de emergencia debe dirigirse a una zona segura", font = "tomas     9",bg="pink")
    etiqueta7.pack(fill = tkinter.X)
    etiqueta8 = tkinter.Label(newWindow, text = "Mensaje 12 s: Cierre todas las ventanas y asegure las puertas.", font = "tomas 9",bg="gray")
    etiqueta8.pack(fill = tkinter.X)
    etiqueta9 = tkinter.Label(newWindow, text = "No utilice el teléfono. Escuche los medios de comunicación ", font = "tomas 9",bg="gray")
    etiqueta9.pack(fill = tkinter.X)
    etiqueta10 = tkinter.Label(newWindow, text = "para más información de las autoridades locales", font = "tomas 9",bg="gray")
    etiqueta10.pack(fill = tkinter.X)

    

    
    boton3 = tkinter.Button(newWindow, text = "Mensaje 2 s", pady = 20,bg="yellow") 
    boton3.pack(side="left")
    boton2 = tkinter.Button(newWindow, text = "mensaje 4 s", pady = 20,bg="white") 
    boton2.pack(side="left")
    boton2 = tkinter.Button(newWindow, text = "mensaje 12 s", pady = 20,bg="gray") 
    boton2.pack(side="left")


def createNewWindow2():
    newWindow2 = tk.Toplevel(root)
    newWindow2.geometry("500x400")
    newWindow2.config(bg="pink")

    etiqueta0 = tkinter.Label(newWindow2, text = "Universidad Distrital ", font = "tomas 15",bg="orange")
    etiqueta0.pack(fill = tkinter.X)

    etiqueta1 = tkinter.Label(newWindow2, text = "Francisco José de Caldas", font = "tomas 15",bg="orange")
    etiqueta1.pack(fill = tkinter.X)

    etiqueta = tkinter.Label(newWindow2, text = "Sistema de transmisión ",bg="white", font = "Verdana 17", pady =5)
    etiqueta4 = tkinter.Label(newWindow2, text = " para FM ",bg="white", font = "Verdana 17", pady =5)

    etiqueta.pack(fill = tkinter.X)
    etiqueta4.pack(fill = tkinter.X)


    etiqueta6 = tkinter.Label(newWindow2, text = "Mensaje 2 s: Estado de Emergencia", font = "tomas 9",bg="yellow")
    etiqueta6.pack(fill = tkinter.X)
    etiqueta7 = tkinter.Label(newWindow2, text = "Mensaje 4 s: Este es un mensaje de emergencia debe dirigirse a una zona segura", font = "tomas     9",bg="pink")
    etiqueta7.pack(fill = tkinter.X)
    etiqueta8 = tkinter.Label(newWindow2, text = "Mensaje 12 s: Cierre todas las ventanas y asegure las puertas.", font = "tomas 9",bg="gray")
    etiqueta8.pack(fill = tkinter.X)
    etiqueta9 = tkinter.Label(newWindow2, text = "No utilice el teléfono. Escuche los medios de comunicación ", font = "tomas 9",bg="gray")
    etiqueta9.pack(fill = tkinter.X)
    etiqueta10 = tkinter.Label(newWindow2, text = "para más información de las autoridades locales", font = "tomas 9",bg="gray")
    etiqueta10.pack(fill = tkinter.X)

    boton3 = tkinter.Button(newWindow2, text = "Mensaje 2 s", pady = 20,bg="yellow") 
    boton3.pack(side="left")
    boton2 = tkinter.Button(newWindow2, text = "mensaje 4 s", pady = 20,bg="pink") 
    boton2.pack(side="left")
    boton2 = tkinter.Button(newWindow2, text = "mensaje 12 s", pady = 20,bg="gray") 
    boton2.pack(side="left")




root =  tkinter.Tk()
root.geometry("500x400")
root.config(bg="pink")

#etiqueta principal
etiqueta0 = tkinter.Label(root, text = "Universidad Distrital Francisco José de Caldas", font = "tomas 15")
etiqueta0.pack(fill = tkinter.X)

#etiquetas pequeñas
etiqueta = tkinter.Label(root, text = "Transmisión de emergencia de ",bg="ORANGE", font = "Helvetica 15", pady =7)
etiqueta4 = tkinter.Label(root, text = " condición crítica mediante ",bg="ORANGE", font = "Helvetica 15", pady =7)
etiqueta5 = tkinter.Label(root, text = "radio cognitiva en redes AM y FM",bg="ORANGE", font = "Helvetica 15", pady =7)
etiqueta.pack(fill = tkinter.X)
etiqueta4.pack(fill = tkinter.X)
etiqueta5.pack(fill = tkinter.X)
	

buttonExample = tk.Button(root, text="Modulación AM",command=createNewWindow)
buttonExample.pack()

buttonExample1 = tk.Button(root, text="Modulación FM",command=createNewWindow2)
buttonExample1.pack()

def cerrar_ventana():
    root.destroy()
    os.system('kill -9 $(pidof -s python)')

button = tk.Button(text = "Salir", command = cerrar_ventana, bg = "blue")
button.pack()

root.mainloop()
