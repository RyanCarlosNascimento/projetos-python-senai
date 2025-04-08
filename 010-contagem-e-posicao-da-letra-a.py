# Crie um programa que leia uma frase e mostre:
# 1. Quantas vezes aparece a letra “a”
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece na última vez

#Leitura de dados
frase = input("Digite uma frase: ").strip().upper() #Tiro espaços antes e depois do que foi digitado.
# Transformo a variavel frase toda em MAIUSCULA
print()

#1. Contagem A(s)

#Substituo todas as variações de A por A com acento.
frase = frase.replace('Á', 'A')
frase = frase.replace('À', 'A')
frase = frase.replace('Â', 'A')
frase = frase.replace('Ã', 'A')


# Retorno de informações
print(f'Sua frase exibiu um total de: {frase.count('A')} letras A(s)'
      f'\n O primeiro A da sua frase está na {frase.find('A') + 1}° posição.' # Desloca um para direita (Caso o primeiro A no 0, agora aparece A)
      f'\n O último A da sua frase está na {frase.rfind('A') + 1}° posição.') # Desloca um para direita (Caso o primeiro A no 0, agora aparece A)