class TarjetaDeCredito:

    def __init__(self,entidadBancaria,numero,titular):

        self.entidadBancaria = entidadBancaria
        self.__numero        = numero
        self.__Versaldo      = 15000
        self.titular         = titular

   


    def informarTitular(self):
        return self.titular.datosTitular()

    def verificar_saldo(self,monto):
        return self.__Versaldo > monto;



    def descontar_saldo(self,monto):
         self.__Versaldo -= monto
    

    @property
    def saldo(self):
        return self.__Versaldo

    @property
    def numero(self):
        return self.__numero


    @numero.setter
    def numero(self, nuevo_numero):
        if nuevo_numero != self.__numero:
            self.__numero = nuevo_numero