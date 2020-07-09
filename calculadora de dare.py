#Sistema de calculo da dare, imposto cobrado pelo posto fiscal em uma mercadoria de uma estado para o outro.
#Calculo GO para RR
#Desenvolvido por Thiago Silva de Oliveira e Aloson Martins
#Coordenador: Thiago Luiz Loreto de Lima
import os
print('Sistema de Calculo de Imposto Interestadual')
print('--------------------------------------------')
print('PROTOCOLO 103/2014')
print('--------------------------------------------')
print("""
MVA ORIGINAL 36.56   MVA ORIGINAL 71.78
12%  44,79           12%  82,13"
4%   57,95           4%   98,69  
7%   53,01           7%   92,48
   """)
print('--------------------------------------------')

print('MVA AJUSTADO')
valor1 = float(input('Informe o percental MVA ST Original: '))
valor2 = float(input('informe a aliquato Interestadual: '))
valor3 = float(input('Qual a aliquota Destino: '))
valor4 = float(input('Qual o valor do produto: '))
valor5 = float(input('Qual valor do IPI: '))
valor6 = float(input('Qual o valor do frete: '))
valor7 = float(input('Qual valor do Seguro: '))
valor8 = float(input('Qual valor de Outras Despesas: '))
valor9 = float(input('Qual o valor do Desconto Suframa: '))
n = valor4 + valor5 + valor6 + valor7 + valor8 - valor9
print('O Total da NF é : {}'.format(n))
n1 = (1 + valor1 / 100)*(1 - valor2 / 100)/(1 - valor3 / 100)-1
print('--------------------------------------------')
print('O percentual do MVA Ajustado e {:.4f} '.format(n1 * 100))
vp = valor4 * valor2
print('ICMS - Operação Propria e {:.2f} '.format(vp / 100))
base = (n) * (1 + n1)
print('Base de Calculo ICMS ST {:.2f} '.format(base))
retido = (base * valor3 / 100)
print('ICMS ST a ser retido: {:.2f} '.format(retido - vp /100))


