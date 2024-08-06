from Persona import Persona
from Tarjeta import TarjetaDeCredito
from Posnet import Posnet

juan = Persona("Juan","Perez","42040302","sadjkas@gmail.com","39998242")

tarjeta1 = TarjetaDeCredito("Banco Guitarra","4548463000677980", juan)




Pago1 =Posnet()
print(Pago1.efectuarPago(tarjeta1,10000,5))