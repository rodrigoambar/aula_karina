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

# pessoa1 = pessoa()
# pessoa1.set_nome("pedro")
# pessoa1.set_idade(18)
# pessoa1.set_altura(1.70)
# pessoa1.imprimir()

#2
def calcular_juros(valor_vista,valor_parcela,qnt_parcelas):
    valor_total_parcelado = valor_parcela * qnt_parcelas
    valor_juros = valor_total_parcelado - valor_vista
    print(f'o valor do juros é {valor_juros} e o valor total parcelado {valor_total_parcelado}')

#calcular_juros(100,25,5)

#3
class Elevador:
    def __init__(self,andar_atual, total_andares,cap_elevador,quant_pessoas, terreo):
        self.andar_atual = andar_atual
        self.total_andares = total_andares
        self.cap_elevador = cap_elevador
        self.quant_pessoas = quant_pessoas
        self.terreo = terreo

    def inicializa(self):
        self.cap_elevador = 0
        self.quant_pessoas = 0
        self.terreo = 0
    def entra(self):
        if self.cap_elevador < 10:
            self.cap_elevador += 1
            print(f"temos {self.cap_elevador} pessoas")
        else:
            print("capacidade máxima")
    def sai(self):
        if self.cap_elevador > 0:
            self.cap_elevador -= 1
            print(f"uma pessoa saiu e agora temos {self.cap_elevador}")
        else:
            print("não tem ninguem para sair")
    def subir(self):
        if self.andar_atual != self.total_andares:
            self.andar_atual += 1
            print(f'subimos para o andar{self.andar_atual}')
        else:
            print(f"não da para subir pois chegamos no {self.andar_atual}")
    def descer(self):
        if self.andar_atual == self.terreo:
            print("não da para descer pro subsolo")
        else:
            print(f"desceu")
    def finalizar(self):
        print("saiu do programa")

elevador = Elevador(0,10,0,0,0)

def menu():
    escolha = ' '
    while escolha != 5:
        escolha = int(input("Escolha qual ação deseja fazer com o elevador:"))
        print(""" Ações do MENU 
              Digite 1 para entrar no elevador
              Digite 2 para sair do elevador
              Digite 3 para subir
              Digite 4 para Descer
              Digite 5 para sair do programa""")
        if escolha == 1:
            elevador.entra()
        if escolha == 2:
            elevador.sai()
        if escolha == 3:
            elevador.subir()
        if escolha == 4:
            elevador.descer()
        if escolha == 5:
            elevador.finalizar()

#menu()

#4
class Funcionario:
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
        self._senha = '1234'

    def autentificar(self):
        s = ''
        while True:
            s = input("Digite a senha do gerente:")
            if s == self._senha:
                print(f'Senha correta, Bem vindo {self.nome}')
                break
            else:
                s = input("Senha negada tente novamente:")
                if s == self._senha:
                    print(f'Senha correta, Bem vindo {self.nome}')
                    break

#Exercício 1
# pessoa1 = pessoa()
# pessoa1.set_nome("pedro")
# pessoa1.set_idade(18)
# pessoa1.set_altura(1.70)
# pessoa1.imprimir()

#Exercício 2
#calcular_juros(100,25,5)

#Exercício 3
elevador = Elevador(0,10,0,0,0)
#menu()

#Exercício 4
#g = Gerente('Pedro',50525101871,2000)
#g.autentificar()

