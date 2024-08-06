from Ticket import Ticket

class Posnet:

    def efectuarPago(self,tarjeta,monto,cant_cuotas):
        ticket = None
        if self.datosValidos(monto,cant_cuotas):
                monto_final = monto + monto * self.recargo_por_cuotas(cant_cuotas)
                if tarjeta.verificar_saldo(monto_final):
                     tarjeta.descontar_saldo(monto_final)
                     ticket = Ticket(tarjeta.informarTitular(),monto_final,self.calcular_importe_cuotas(cant_cuotas,monto_final))
        return ticket



    def datosValidos(tarjeta,monto,cant_cuotas):
        return monto > 0 and cant_cuotas >0 and cant_cuotas <7
     
     
    def recargo_por_cuotas(self,cant_cuotas):
        return (cant_cuotas-1) * 0.03
            

    def calcular_importe_cuotas(self,cant_cuotas,monto):
         return monto/cant_cuotas




         