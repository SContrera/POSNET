class Ticket:

    def __init__(self,nombre_completo,monto_final,cuotas):
        self.nombre = nombre_completo
        self.monto_total=monto_final
        self.monto_de_Cuotas= cuotas
        
    def __str__(self):
        return f"{self.nombre}, Total de la compra ${self.monto_total},Cuota 1/5{self.monto_de_Cuotas}"