class Complejo:
    def __init__(self,real,imaginario):
        self.real=real
        self.imaginario=imaginario
        #self.norma

    def conjugado(self):
        self.imaginario=-self.imaginario

    def calcula_norma(self):
        self.norma=(self.real**2+self.imaginario**2)**(1/2)

    def pow(self,n):
        t=(self.real+self.imaginario*1j)**n
        return Complejo(t.real,t.imag)