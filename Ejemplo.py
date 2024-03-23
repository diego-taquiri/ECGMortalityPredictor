class Articulo:
    def __init__(self,cd,ct,pr):

        #se inicializan los atributos y se almacenan en los datos
        self.cod=cd
        self.cant=ct
        self.pre=pr
        
    def cantidad(self):
        print('Cantidad actual: ',self.cant)
        
    def precio(self):
        print('Precio:',self.pre)
        
    def vender(self,x):
        if x<=self.cant:
            self.cant=self.cant-x
        else:
            print('Cantidad insuficiente')
            
    def comprar(self,x):
        self.cant=self.cant+x
