# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#Importação de biblioteca
from datetime import date

#Leitura de dados
ano = int(input('Qual ano deseja analisar? Digite "0" caso queira analisar o ano atual: '))

#Condicionais + Retorno de informações
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'\033[32mO ano {ano} é bissexto')
else:
    print(f'\033[31mO ano {ano} NÃO é bissexto')