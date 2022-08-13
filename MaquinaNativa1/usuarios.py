class Usuario():
    
    numUsers = 0
    
    def __init__(self,name,password):
        self.name = name
        self.password = password
        
        self.conected = False
        self.attempts = 3
        
        Usuario.numUsers += 1
        
    def connect(self,password=None):
        if password==None:
            myPass = input("Ingrese su contraseña: ")
        else:
            myPass = password
        if myPass == self.password:
            print("Se ha conectado con éxito!!")
            self.conected = True
            return True
        else:
            self.attempts -= 1
            if self.attempts > 0:
                print("Contraseña incorrecta, intentelo de vuelta")
                if password!=None:
                    return False
                print("Intentos restantes: ",self.attempts)
                self.connect()
            else:
                print("Error, no se pudo iniciar sesión. Adiós")
            
    def disconnect(self):
        if self.conected:
            print("Se cerró sesión con éxito!!!")
            self.conected = False
        else:
            print("Error, no inició sesión")
    
    def __str__(self):
        if self.conected:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es {self.name} y estoy {conect}"

# user1 = Usuario(input("Ingrese un nombre: "),input("Ingrese una contraseña: "))
# print(user1)

# user1.connect()
# print(user1)

# user1.disconnect()
# print(user1)