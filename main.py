class Auto:

    cantidadCreados= 0 #Todavía no se han creado carros


    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1 #Se acaba de crear un carro, por lo que se suma uno al contador


    def cantidadAsientos(self):

        return sum(1 for sillin in self.asientos if isinstance(sillin, Asiento)) #Se retorna la suma de cada uno de los asientos en el carro, siempre y cuando el asiento sea un asiento.
    

    def verificarIntegridad(self):
        
        losAsientosEstanOk=True #Asumir que los asientos estan bien

        for asientoPorVerificar in self.asientos: #Se pasa por cada asiento
           
            if (isinstance(asientoPorVerificar, Asiento) and asientoPorVerificar!=None): #Verificar que si sea un asiento y no un nulo
              
                if (asientoPorVerificar.registro !=self.registro): #Si los registros del auto y el asiento no coinciden...
                   
                    losAsientosEstanOk=False #... Ya los asientos no están ok
        

        if ((self.motor!=None) and (self.motor.registro==self.registro)and (losAsientosEstanOk==True)): #Verificar que el motor no es nulo ^ el registro del motor es correcto ^ asientos estan bien.
           
            return 'Auto original' #Si todo eso se cumple el auto es original
        
        else: 
            return 'Las piezas no son originales' #sino entonces no



class Motor:

    def __init__(self, numeroCilindros, tipo, registro):

        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro
        

    def cambiarRegistro(self, nuevoRegistro):

        self.registro=nuevoRegistro; #cambiar el registro por uno nuevo llamado nuevoRegistro


    def asignarTipo(self, nuevoTipo: str):

        if nuevoTipo.lower() in {"gasolina", "eléctrico", "electrico"}: #Asegurarse de que solo se pueda elegir entre motor a gasolina, eléctrico o electrico.

            self.tipo=nuevoTipo



class Asiento:
    
    def __init__(self, color, precio, registro):

        self.color=color
        self.precio=precio
        self.registro=registro


    def cambiarColor(self,colorQueDeseaLaPersona: str):

        coloresQueEstanPermitidosParaLosAsientos={"rojo","verde","amarillo","negro","blanco"} #Solo se puede cambiar el color de los asientos por uno de estos

        if colorQueDeseaLaPersona.lower() in coloresQueEstanPermitidosParaLosAsientos:

            self.color=colorQueDeseaLaPersona

