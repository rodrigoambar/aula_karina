#1 
class pessoa:
    def __init__(self):
        self._nome = ""
        self._idade = 0
        self._altura = 0.0
    def set_nome(self,nome):
        self._nome = nome

    def set_idade(self,idade):
        self._idade = idade
    
    def set_altura(self,altura):
        self._altura = altura
    
    def imprimir(self):
        print(f'a pessoa se chama :{self._nome}, tem {self._idade} anos e {self._altura} m de altura')

pessoa1 = pessoa()
pessoa1.set_nome("pedro")
pessoa1.set_idade(18)
pessoa1.set_altura(1.70)
pessoa1.imprimir()

#2
def calcular_juros(valor_vista,valor_parcela,qnt_parcelas):
    valor_total_parcelado = valor_parcela * qnt_parcelas
    valor_juros = valor_total_parcelado - valor_vista
    print(f'o valor do juros é {valor_juros} e o valor total parcelado {valor_total_parcelado}')

calcular_juros(100,25,5)


