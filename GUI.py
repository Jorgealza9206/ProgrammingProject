import tkinter

ventana = tkinter.Tk()
ventana.geometry("250x400")
ventana.config(bg="black")

img = tkinter.PhotoImage(file = "logo_ud.png")
lbl_img = tkinter.Label(ventana, image = img)
lbl_img.place(x= 10, y = 10)

def Button():
	exec(open("Master-RX.py").read())

boton1 = tkinter.Button(ventana, text = "SINTONIZAR",width = 8, height= 1, bg = "red", fg = "white", command = Button)
boton1.place(x = 80, y = 350)

ventana.mainloop()