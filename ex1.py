# 1 
# Escreva uma classe Complexo que permita representar números complexos e ao menos os métodos:
# · __init__ (esse precisa estar presente em todas as classes)
# · soma
# · multiplicação
# · __str__, que retorna um string na forma a+bj (ou a-bj), onde a e b são as partes real e imaginária do número complexo.

class complexo:
    def __init__(self, part_real, part_imagi):
       self.part_real = part_real
       self.part_imagi = part_imagi
    
    def somar_complexo(self):
        n1 = complex(self.part_real, self.part_imagi)
        soma = n1 + n1
        print(soma)
    
    def multiplica_complexo(self):
        n1 = complex(self.part_real, self.part_imagi)
        multi = n1 * n1
        print(multi)

    def __str__(self):
            if self.part_imagi > 0:
                print(str(f'{self.part_real} + {self.part_imagi}j'))
            else:
                 print(str(f'{self.part_real}{self.part_imagi}j'))

a = complexo(12, 2)
a.somar_complexo()
a.multiplica_complexo()
a.__str__()
